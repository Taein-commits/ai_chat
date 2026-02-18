from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam
from mysql_class import MySQLMemory
from dotenv import load_dotenv
from typing import Dict, Optional, Generator, List, Any, cast
import os

load_dotenv()


class ChatbotAI:

    # --------------------------------------------------
    # INIT
    # --------------------------------------------------
    def __init__(
        self,
        model: str,
        system_prompt: str,
        key: Optional[str] = None
    ) -> None:

        self.model: str = model
        self.client: OpenAI = OpenAI(api_key=key) if key else OpenAI()

        self.messages: List[Dict[str, Any]] = [
            {"role": "system", "content": system_prompt}
        ]

        self.reply: str = ""
        self.last_usage: Optional[Dict[str, int]] = None
        self.total_tokens: int = 0
        self.total_cost: float = 0.0

        self.memory: MySQLMemory = MySQLMemory(
            host=os.getenv("MYSQL_HOST", "localhost"),
            user=os.getenv("MYSQL_USER", "root"),
            password=os.getenv("MYSQL_PASSWORD") or "",
            database=os.getenv("MYSQL_DATABASE", "aimemory")
        )

    # --------------------------------------------------
    # UPDATE SYSTEM PROMPT
    # --------------------------------------------------
    def update_system_prompt(self, new_prompt: str) -> None:
        self.messages = [
            {"role": "system", "content": new_prompt}
        ]

    # --------------------------------------------------
    # CREATE EMBEDDING
    # --------------------------------------------------
    def create_embedding(self, text: str) -> List[float]:
        response = self.client.embeddings.create(
            model="text-embedding-3-small",
            input=text
        )
        return response.data[0].embedding

    # --------------------------------------------------
    # REMOVE OLD MEMORY BLOCK
    # --------------------------------------------------
    def clear_memory_block(self) -> None:
        self.messages = [
            m for m in self.messages
            if not (
                m.get("role") == "system"
                and "Relevant past memory:" in str(m.get("content"))
            )
        ]

    # --------------------------------------------------
    # STREAMING CHAT (WITH MEMORY + COST)
    # --------------------------------------------------
    def chat(
        self,
        text: str,
        temperature: float = 0.7,
        user_id: str = "default_user"
    ) -> Generator[str, None, None]:

        self.messages.append({"role": "user", "content": text})

        query_embedding: List[float] = self.create_embedding(text)
        memories: List[str] = self.memory.retrieve_memory(user_id, query_embedding)

        self.clear_memory_block()

        if memories:
            memory_block: str = "\n\n".join(memories)
            self.messages.insert(1, {
                "role": "system",
                "content": f"Relevant past memory:\n{memory_block}"
            })

        response = self.client.chat.completions.create(
            model=self.model,
            messages=cast(List[ChatCompletionMessageParam], self.messages),
            temperature=temperature,
            stream=True
        )

        full_reply: str = ""

        for chunk in response:
            if not hasattr(chunk, "choices"):
                continue

            if not chunk.choices:
                continue

            delta = chunk.choices[0].delta

            content = getattr(delta, "content", None)

            if content is not None:
                full_reply += content
                yield full_reply

            usage = getattr(chunk, "usage", None)

            if usage is not None:
                self.last_usage = {
                    "prompt_tokens": usage.prompt_tokens,
                    "completion_tokens": usage.completion_tokens,
                    "total_tokens": usage.total_tokens
                }

        self.memory.save_memory(
            user_id,
            f"User: {text}\nAssistant: {full_reply}",
            query_embedding
        )

        if self.last_usage:
            self.total_tokens += int(self.last_usage["total_tokens"])
            self.total_cost += float(self.calculate_cost(self.last_usage))

        self.reply = full_reply
        self.messages.append({"role": "assistant", "content": full_reply})

        self.trim_memory()

    # --------------------------------------------------
    # AGENT MODE
    # --------------------------------------------------
    def agent_chat(
        self,
        text: str,
        temperature: float = 0.7,
        max_steps: int = 3
    ) -> Generator[str, None, None]:

        self.messages.append({"role": "user", "content": text})

        for _ in range(max_steps):
            response = self.client.chat.completions.create(
                model=self.model,
                messages=cast(List[ChatCompletionMessageParam], self.messages),
                temperature=temperature
            )

            message = response.choices[0].message

            if not message.tool_calls:
                final_answer: str = message.content or ""
                self.messages.append({
                    "role": "assistant",
                    "content": final_answer
                })
                yield final_answer
                break

            tool_call = message.tool_calls[0]

            if not hasattr(tool_call, "function"):
                return

            function_obj = tool_call.function

            tool_name: str = function_obj.name
            arguments: str = function_obj.arguments

            result: float | str = self.execute_tool(tool_name, arguments)

            self.messages.append({
                "role": "assistant",
                "content": message.content or ""
            })

            self.messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": str(result)
            })

        self.trim_memory()

    # --------------------------------------------------
    # TOOL EXECUTION
    # --------------------------------------------------
    def execute_tool(self, name: str, arguments: str) -> float | str:
        import json
        args: Dict[str, Any] = json.loads(arguments)

        if name == "calculate_bmi":
            height: float = args["height_cm"] / 100
            weight: float = args["weight_kg"]
            bmi: float = weight / (height ** 2)
            return round(bmi, 2)

        return "Tool not implemented"

    # --------------------------------------------------
    # COST CALCULATOR
    # --------------------------------------------------
    def calculate_cost(self, usage: Dict[str, int]) -> float:

        pricing: Dict[str, float] = {
            "gpt-4.1-mini": 0.000002,
            "gpt-4o-mini": 0.0000015,
            "gpt-4o": 0.00001
        }

        price_per_token: float = pricing.get(self.model, 0.000002)

        return float(usage["total_tokens"]) * price_per_token

    # --------------------------------------------------
    # MEMORY TRIM
    # --------------------------------------------------
    def trim_memory(self) -> None:
        MAX_MESSAGES: int = 20
        if len(self.messages) > MAX_MESSAGES:
            self.messages = [self.messages[0]] + self.messages[-MAX_MESSAGES:]
