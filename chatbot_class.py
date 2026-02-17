from openai import OpenAI

class ChatbotAI:
    def __init__(self, model, system_prompt, key=None):
        self.model = model
        self.client = OpenAI(api_key=key) if key else OpenAI()
        self.messages = [
            {"role": "system", "content": system_prompt}
        ]
        self.reply = ""
        
    def update_system_prompt(self, new_prompt):
        self.messages = [
            {"role": "system", "content": new_prompt}
        ]    

    def add_user_input(self, text, temperature=0.5):
        self.messages.append({"role": "user", "content": text})

        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages,
            temperature=temperature
            stream=True
        )

        full_reply = ""

        for chunk in response:
            if chunk.choices[0].delta.content:
                full_reply += chunk.choices[0].delta.content
                yield full_reply   # 🔥 IMPORTANT

        self.reply = full_reply
        self.messages.append({"role": "assistant", "content": self.reply})
        
        # Memory trim (keep last 20 messages)
        MAX_MESSAGES = 20
        if len(self.messages) > MAX_MESSAGES:
            self.messages = [self.messages[0]] + self.messages[-MAX_MESSAGES:]

    def get_reply(self):
        return self.reply