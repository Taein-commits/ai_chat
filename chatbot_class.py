from openai import OpenAI
from mysql_class import MySQLMemory
from dotenv import load_dotenv
import os

load_dotenv()

class ChatbotAI:

    # --------------------------------------------------
    # INIT
    # --------------------------------------------------
    def __init__(self, model, system_prompt, key=None):

        self.model = model
        self.client = OpenAI(api_key=key) if key else OpenAI()

        self.messages = [
            {"role": "system", "content": system_prompt}
        ]

        self.reply = ""
        self.last_usage = None
        self.total_tokens = 0
        self.total_cost = 0.0

        # MySQL Vector Memory
        self.memory = MySQLMemory(
            host=os.getenv("MYSQL_HOST", "localhost"),
            user=os.getenv("MYSQL_USER", "root"),
            password=os.getenv("MYSQL_PASSWORD"),
            database=os.getenv("MYSQL_DATABASE", "aimemory")
        )

    # --------------------------------------------------
    # UPDATE SYSTEM PROMPT
    # --------------------------------------------------
    def update_system_prompt(self, new_prompt):
        self.messages = [
            {"role": "system", "content": new_prompt}
        ]

    # --------------------------------------------------
    # CREATE EMBEDDING
    # --------------------------------------------------
    def create_embedding(self, text):
        response = self.client.embeddings.create(
            model="text-embedding-3-small",
            input=text
        )
        return response.data[0].embedding

    # --------------------------------------------------
    # REMOVE OLD MEMORY BLOCK
    # --------------------------------------------------
    def clear_memory_block(self):
        self.messages = [
            m for m in self.messages
            if not (m["role"] == "system" and "Relevant past memory:" in m["content"])
        ]

    # --------------------------------------------------
    # STREAMING CHAT (WITH MEMORY + COST)
    # --------------------------------------------------
    def chat(self, text, temperature=0.7, user_id="default_user"):

        self.messages.append({"role": "user", "content": text})

        # -------- Vector Retrieval --------
        query_embedding = self.create_embedding(text)
        memories = self.memory.retrieve_memory(user_id, query_embedding)

        self.clear_memory_block()

        if memories:
            memory_block = "\n\n".join(memories)
            self.messages.insert(1, {
                "role": "system",
                "content": f"Relevant past memory:\n{memory_block}"
            })

        # -------- Streaming Response --------
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages,
            temperature=temperature,
            stream=True
        )

        full_reply = ""

        for chunk in response:
            if chunk.choices[0].delta.content:
                full_reply += chunk.choices[0].delta.content
                yield full_reply

            # Capture usage at final chunk
            if chunk.usage:
                self.last_usage = {
                    "prompt_tokens": chunk.usage.prompt_tokens,
                    "completion_tokens": chunk.usage.completion_tokens,
                    "total_tokens": chunk.usage.total_tokens
                }

        # -------- Save Memory --------
        self.memory.save_memory(
            user_id,
            f"User: {text}\nAssistant: {full_reply}",
            query_embedding
        )

        # -------- Cost Calculation --------
        if self.last_usage:
            self.total_tokens += self.last_usage["total_tokens"]
            self.total_cost += self.calculate_cost(self.last_usage)

        self.reply = full_reply
        self.messages.append({"role": "assistant", "content": full_reply})

        self.trim_memory()

    # --------------------------------------------------
    # AGENT MODE
    # --------------------------------------------------
    def agent_chat(self, text, temperature=0.7, max_steps=3):

        self.messages.append({"role": "user", "content": text})

        for step in range(max_steps):

            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.messages,
                temperature=temperature
            )

            message = response.choices[0].message

            if not message.tool_calls:
                final_answer = message.content
                self.messages.append({
                    "role": "assistant",
                    "content": final_answer
                })
                yield final_answer
                break

            tool_call = message.tool_calls[0]
            tool_name = tool_call.function.name
            arguments = tool_call.function.arguments

            result = self.execute_tool(tool_name, arguments)

            self.messages.append(message)
            self.messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": str(result)
            })

        self.trim_memory()

    # --------------------------------------------------
    # TOOL EXECUTION
    # --------------------------------------------------
    def execute_tool(self, name, arguments):
        import json
        args = json.loads(arguments)

        if name == "calculate_bmi":
            height = args["height_cm"] / 100
            weight = args["weight_kg"]
            bmi = weight / (height ** 2)
            return round(bmi, 2)

        return "Tool not implemented"

    # --------------------------------------------------
    # COST CALCULATOR (ESTIMATED)
    # --------------------------------------------------
    def calculate_cost(self, usage):

        pricing = {
            "gpt-4.1-mini": 0.000002,
            "gpt-4o-mini": 0.0000015,
            "gpt-4o": 0.00001
        }

        price_per_token = pricing.get(self.model, 0.000002)

        return usage["total_tokens"] * price_per_token

    # --------------------------------------------------
    # MEMORY TRIM
    # --------------------------------------------------
    def trim_memory(self):
        MAX_MESSAGES = 20
        if len(self.messages) > MAX_MESSAGES:
            self.messages = [self.messages[0]] + self.messages[-MAX_MESSAGES:]
