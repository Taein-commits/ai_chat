from openai import OpenAI
from tool_registry import TOOLS, TOOL_FUNCTIONS
import json

class ChatbotAI:
    def __init__(self, model, system_prompt, key=None):
        self.model = model
        self.client = OpenAI(api_key=key) if key else OpenAI()
        self.messages = [
            {"role": "system", "content": system_prompt}
        ]
        self.last_usage = None

    def update_system_prompt(self, new_prompt):
        self.messages = [
            {"role": "system", "content": new_prompt}
        ]

    def add_user_input(self, text, temperature=0.5):
        self.messages.append({"role": "user", "content": text})

        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages,
            tools=TOOLS,
            tool_choice="auto",
            temperature=temperature
        )

        message = response.choices[0].message

        # 🔥 If tool call detected
        if message.tool_calls:
            tool_call = message.tool_calls[0]
            tool_name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)

            # Execute tool
            result = TOOL_FUNCTIONS[tool_name](**arguments)

            # Add tool result to conversation
            self.messages.append(message)
            self.messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": json.dumps(result)
            })

            # Ask model to generate final answer using tool result
            final_response = self.client.chat.completions.create(
                model=self.model,
                messages=self.messages,
                temperature=temperature
            )

            final_message = final_response.choices[0].message.content
            self.messages.append({
                "role": "assistant",
                "content": final_message
            })

            self.last_usage = final_response.usage
            return final_message

        else:
            # Normal response
            reply = message.content
            self.messages.append({
                "role": "assistant",
                "content": reply
            })
            self.last_usage = response.usage
            return reply
