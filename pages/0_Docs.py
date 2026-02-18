# pages/docs.py

import streamlit as st

st.set_page_config(page_title="Documentation", page_icon="📚")

st.title("📚 My AI Assistant - Documentation")

st.markdown("---")

# =========================
# 1️⃣ How To Use
# =========================
st.header("🚀 How To Use")

st.markdown("""
1. Select a **Mode** from the sidebar.
2. Choose a **Model** (Fast, Smart, Reasoning, Budget).
3. Adjust **Temperature** if needed.
4. Type your message in the chat box.
5. Watch streaming response in real-time.
""")

st.markdown("---")

# =========================
# 2️⃣ Modes
# =========================
st.header("🧠 Modes Explained")

st.markdown("""
| Mode | Description |
|------|-------------|
| General | Normal AI assistant |
| Coder | Programming & debugging |
| Medical | Clinical & USMLE explanations |
| English Trainer | Grammar correction & conversation |
| Draw 🎨 | AI image generation |
""")

st.markdown("---")

# =========================
# 3️⃣ Model Comparison
# =========================
st.header("🤖 Model Guide")

st.markdown("""
| Model | Speed | Intelligence | Cost |
|-------|--------|-------------|------|
| gpt-4o-mini | ⚡ Very Fast | Good | 💰 Low |
| gpt-4o | Balanced | High | 💰💰 |
| gpt-4.1 | Advanced Reasoning | Very High | 💰💰💰 |
| gpt-4.1-mini | Budget reasoning | Medium | 💰 |
""")

st.info("Use gpt-4o-mini for daily chat. Use gpt-4.1 for deep reasoning.")

st.markdown("---")

# =========================
# 4️⃣ Agent Mode
# =========================
st.header("🧩 Agent Mode")

st.markdown("""
Agent Mode allows multi-step reasoning.
The AI can:
- Call tools (BMI calculator, math, etc.)
- Think step-by-step
- Perform intermediate operations
""")

st.markdown("---")

# =========================
# 5️⃣ Document Upload
# =========================
st.header("📂 Document Upload")

st.markdown("""
You can upload:
- PDF
- CSV
- TXT

The AI will:
- Inject document into context
- Answer based on your file
- Generate charts from CSV data
""")

st.markdown("---")

# =========================
# 6️⃣ Cost Tracking
# =========================
st.header("💰 Cost Tracking")

st.markdown("""
The system calculates:
- Input tokens
- Output tokens
- Cost per model

Session cost is displayed in sidebar.
""")

st.markdown("---")

# =========================
# 7️⃣ Environment Setup
# =========================
st.header("🔐 Environment Setup")

st.code("""
# .env example

OPENAI_API_KEY=your_key_here
MYSQL_HOST=localhost
MYSQL_USER=aiuser
MYSQL_PASSWORD=your_password
MYSQL_DATABASE=aimemory
""")

st.success("You are now using a professional multi-page AI platform.")
