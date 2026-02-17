from openai import OpenAI

class ChatbotAI:
    def __init__(self, model, system_prompt, key=None):
        self.model = model
        self.client = OpenAI(api_key=key) if key else OpenAI()
        self.messages = [
            {"role": "system", "content": system_prompt}
        ]
        self.reply = ""
        self.total_tokens = 0
        self.total_cost = 0.0

    def update_system_prompt(self, new_prompt):
        self.messages = [
            {"role": "system", "content": new_prompt}
        ]

    # --------------------------------------------------
    # NORMAL CHAT MODE
    # --------------------------------------------------
    def chat(self, text, temperature=0.5):
        self.messages.append({"role": "user", "content": text})

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

        self.reply = full_reply
        self.messages.append({"role": "assistant", "content": full_reply})

        self.trim_memory()

    # --------------------------------------------------
    # AGENT MODE (Multi-step reasoning)
    # --------------------------------------------------
    def agent_chat(self, text, temperature=0.5, max_steps=3):
        self.messages.append({"role": "user", "content": text})

        for step in range(max_steps):

            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.messages,
                temperature=temperature,
            )

            message = response.choices[0].message

            # If no tool calls → final answer
            if not message.tool_calls:
                final_answer = message.content
                self.messages.append(
                    {"role": "assistant", "content": final_answer}
                )
                yield final_answer
                break

            # Tool call detected
            tool_call = message.tool_calls[0]
            tool_name = tool_call.function.name
            arguments = tool_call.function.arguments

            tool_result = self.execute_tool(tool_name, arguments)

            self.messages.append(message)
            self.messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": str(tool_result),
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
    def trim_memory(self):
        MAX_MESSAGES = 20
        if len(self.messages) > MAX_MESSAGES:
            self.messages = [self.messages[0]] + self.messages[-MAX_MESSAGES:]
