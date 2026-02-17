import streamlit as st
import base64, re
from io import BytesIO
from PIL import Image
from chatbot_class import ChatbotAI
from style import style

st.set_page_config(page_title="My AI Chatbot By Taein Kim", page_icon="🤖")

def render_response(text):
    code_blocks = re.findall(r"```(.*?)```", text, re.DOTALL)

    if code_blocks:
        parts = re.split(r"```.*?```", text, flags=re.DOTALL)

        for i, part in enumerate(parts):
            if part.strip():
                st.markdown(part)

            if i < len(code_blocks):
                code_content = code_blocks[i]

                # Try to detect language
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

MODES = {
    "General": "You are a helpful AI assistant.",
    "Coder": "You are an expert Python, Arduino, and software engineer. Give clean code with explanation.",
    "Medical": "You are a clinical medical tutor helping prepare for USMLE exams. Explain clearly and structured.",
    "English Trainer": "You help improve English speaking. Correct grammar gently and suggest better sentences.",
    "Draw 🎨": "You generate creative image prompts.",
}

# -------------------------
# Streamlit GUI
# -------------------------
st.markdown(style, unsafe_allow_html=True)

st.markdown("""
<h1 style='
text-align:center;
font-size:48px;
font-weight:800;
background: linear-gradient(90deg, #38bdf8, #6366f1);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
margin-bottom: 10px;
'>
🤖 My AI Assistant By Taein Kim
</h1>
""", unsafe_allow_html=True)

st.sidebar.title("⚙ Settings")
selected_mode = st.sidebar.selectbox("Mode", list(MODES.keys()))    

# Create chatbot only once (important!)
if "bot" not in st.session_state:
    st.session_state.bot = ChatbotAI(model="gpt-4o-mini", system_prompt=MODES[selected_mode])
    st.session_state.current_mode = selected_mode

bot = st.session_state.bot

# Display previous messages
for msg in bot.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            if msg["role"] == "assistant":
                render_response(msg["content"])
            else:
                st.markdown(msg["content"])

if "current_mode" not in st.session_state:
    st.session_state.current_mode = selected_mode

if selected_mode != st.session_state.current_mode:
    st.session_state.bot.update_system_prompt(MODES[selected_mode])
    st.session_state.current_mode = selected_mode

# Chat input
if prompt := st.chat_input("Type your message..."):
    
    # Show user message
    with st.chat_message("user"):
        st.markdown(prompt)

    if selected_mode == "Draw 🎨":
        with st.chat_message("assistant"):
            with st.spinner("Generating image..."):
                st.image(Image.open(BytesIO(base64.b64decode(bot.client.images.generate(model="gpt-image-1",prompt=prompt,size="1024x1024").data[0].b64_json))))
                
        # Save to memory
        bot.messages.append({
            "role": "assistant",
            "content": f"[Generated image for prompt: {prompt}]"
        })        
    else:             
        with st.chat_message("assistant"):
            placeholder = st.empty()
            full_text = ""

            for partial in bot.add_user_input(prompt):
                full_text = partial
                placeholder.markdown(full_text)

            # After streaming finishes, render properly
            placeholder.empty()
            render_response(full_text)

