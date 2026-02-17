import streamlit as st
import base64, re, pandas as pd
from io import BytesIO
from PIL import Image
from PyPDF2 import PdfReader
from chatbot_class import ChatbotAI
from style import style

# -------------------------
# Page Config (MUST BE FIRST)
# -------------------------
st.set_page_config(
    page_title="My AI Assistant By Taein Kim",
    page_icon="🤖"
)

st.markdown(style, unsafe_allow_html=True)

# -------------------------
# Pricing Table (per 1K tokens)
# -------------------------
MODEL_PRICING = {
    "gpt-4o-mini": {"input": 0.00015, "output": 0.0006},
    "gpt-4o": {"input": 0.005, "output": 0.015},
    "gpt-4.1": {"input": 0.01, "output": 0.03},
    "gpt-4.1-mini": {"input": 0.0003, "output": 0.0012},
}

# -------------------------
# Modes
# -------------------------
MODES = {
    "General": "You are a helpful AI assistant.",
    "Coder": "You are an expert Python, Arduino developer.",
    "Medical": "You are a clinical medical tutor.",
    "English Trainer": "You help improve English speaking.",
    "Draw 🎨": "You generate creative image prompts.",
}

# -------------------------
# Render Code Blocks
# -------------------------
def render_response(text):
    code_blocks = re.findall(r"```(.*?)```", text, re.DOTALL)

    if code_blocks:
        parts = re.split(r"```.*?```", text, flags=re.DOTALL)

        for i, part in enumerate(parts):
            if part.strip():
                st.markdown(part)

            if i < len(code_blocks):
                code_content = code_blocks[i]
                first_line = code_content.strip().split("\n")[0]

                if first_line.isalpha():
                    language = first_line
                    code_body = "\n".join(code_content.split("\n")[1:])
                else:
                    language = "python"
                    code_body = code_content

                st.code(code_body, language=language)
    else:
        st.markdown(text)

# -------------------------
# Sidebar Controls
# -------------------------

agent_mode = st.sidebar.checkbox("Agent Mode", value=False)

st.sidebar.title("⚙ Settings")

selected_mode = st.sidebar.selectbox("Mode", list(MODES.keys()))

MODEL_OPTIONS = {
    "⚡ Fast (gpt-4o-mini)": "gpt-4o-mini",
    "🧠 Smart (gpt-4o)": "gpt-4o",
    "🔬 Reasoning (gpt-4.1)": "gpt-4.1",
    "💰 Budget (gpt-4.1-mini)": "gpt-4.1-mini"
}

selected_model_label = st.sidebar.selectbox(
    "Model",
    list(MODEL_OPTIONS.keys())
)

selected_model = MODEL_OPTIONS[selected_model_label]

temperature = st.sidebar.slider(
    "Creativity (Temperature)",
    0.0, 1.5, 0.7, 0.1
)

st.sidebar.markdown("---")
st.sidebar.subheader("📂 Upload Document")

uploaded_file = st.sidebar.file_uploader(
    "Upload PDF or CSV",
    type=["pdf", "csv", "txt"]
)

document_text = None

if uploaded_file is not None:
    file_type = uploaded_file.name.split(".")[-1]

    if file_type == "pdf":
        reader = PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        document_text = text

    elif file_type == "csv":
        df = pd.read_csv(uploaded_file)
        st.session_states.df = df
        document_text = df.to_string()

    elif file_type == "txt":
        document_text = uploaded_file.read().decode("utf-8")

    st.sidebar.success("Document loaded successfully!")
    
# -------------------------
# Initialize Session Cost
# -------------------------
if "total_cost" not in st.session_state:
    st.session_state.total_cost = 0

# -------------------------
# Initialize Bot
# -------------------------
if "bot" not in st.session_state:
    st.session_state.bot = ChatbotAI(
        model=selected_model,
        system_prompt=MODES[selected_mode]
    )
    st.session_state.current_mode = selected_mode
    st.session_state.current_model = selected_model

bot = st.session_state.bot
if document_text:
    bot.load_document(document_text)

# -------------------------
# Detect Model Change
# -------------------------
if selected_model != st.session_state.current_model:
    st.session_state.bot = ChatbotAI(
        model=selected_model,
        system_prompt=MODES[selected_mode]
    )
    st.session_state.current_model = selected_model
    st.rerun()

# -------------------------
# Detect Mode Change
# -------------------------
if selected_mode != st.session_state.current_mode:
    st.session_state.bot = ChatbotAI(
        model=selected_model,
        system_prompt=MODES[selected_mode]
    )
    st.session_state.current_mode = selected_mode
    st.rerun()

# -------------------------
# Title
# -------------------------
st.markdown("""
<h1 style='
text-align:center;
font-size:48px;
font-weight:800;
background: linear-gradient(90deg, #38bdf8, #6366f1);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
'>
🤖 My AI Assistant By Taein Kim
</h1>
""", unsafe_allow_html=True)

# -------------------------
# Display History
# -------------------------
for msg in bot.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            if msg["role"] == "assistant":
                render_response(msg["content"])
            else:
                st.markdown(msg["content"])

# -------------------------
# Chat Input
# -------------------------
if prompt := st.chat_input("Type your message..."):

    with st.chat_message("user"):
        st.markdown(prompt)

    if selected_mode == "Draw 🎨":

        with st.chat_message("assistant"):
            with st.spinner("Generating image..."):

                result = bot.client.images.generate(
                    model="gpt-image-1",
                    prompt=prompt,
                    size="1024x1024"
                )

                image_data = result.data[0].b64_json
                image_bytes = base64.b64decode(image_data)
                image = Image.open(BytesIO(image_bytes))

                st.image(image)

                st.download_button(
                    "⬇ Download Image",
                    image_bytes,
                    file_name="ai_image.png",
                    mime="image/png"
                )

        bot.messages.append({
            "role": "assistant",
            "content": f"[Generated image for prompt: {prompt}]"
        })

    else:

        with st.chat_message("assistant"):
            placeholder = st.empty()
            full_text = ""

            if agent_mode: gen = bot.agent_chat(prompt, temperature=temperature)
            else: bot.chat(prompt, temperature=temperature)
            for partial in gen:
                full_text = partial
                placeholder.markdown(full_text)

            placeholder.empty()
            render_response(full_text)

        # -------------------------
        # COST CALCULATION
        # -------------------------
        if bot.last_usage:

            input_tokens = bot.last_usage.prompt_tokens
            output_tokens = bot.last_usage.completion_tokens
            total_tokens = bot.last_usage.total_tokens

            pricing = MODEL_PRICING[selected_model]

            cost = (
                (input_tokens / 1000) * pricing["input"] +
                (output_tokens / 1000) * pricing["output"]
            )

            st.session_state.total_cost += cost

            st.caption(
                f"Tokens: {total_tokens} | "
                f"Cost: ${cost:.6f}"
            )

# -------------------------
# Sidebar Cost Display
# -------------------------
st.sidebar.title("💰 Session Cost")
st.sidebar.metric(
    "Total Cost",
    f"${st.session_state.total_cost:.4f}"
)
