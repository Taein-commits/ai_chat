# config.py

MODEL_PRICING = {
    "gpt-4o-mini": {"input": 0.00015, "output": 0.0006},
    "gpt-4o": {"input": 0.005, "output": 0.015},
    "gpt-4.1": {"input": 0.01, "output": 0.03},
    "gpt-4.1-mini": {"input": 0.0003, "output": 0.0012},
}

MODES = {
    "General": "You are a helpful AI assistant.",
    "Coder": "You are an expert Python, Arduino developer.",
    "Medical": "You are a clinical medical tutor.",
    "English Trainer": "You help improve English speaking.",
    "Draw 🎨": "You generate creative image prompts.",
}

MODEL_OPTIONS = {
    "⚡ Fast (gpt-4o-mini)": "gpt-4o-mini",
    "🧠 Smart (gpt-4o)": "gpt-4o",
    "🔬 Reasoning (gpt-4.1)": "gpt-4.1",
    "💰 Budget (gpt-4.1-mini)": "gpt-4.1-mini"
}
