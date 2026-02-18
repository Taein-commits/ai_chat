# main.py

import streamlit as st
from chatbot_class import ChatbotAI
from config import MODEL_PRICING, MODES, MODEL_OPTIONS
from ui.layout import setup_page, render_title
from ui.render import render_response
from features.charts import generate_chart
from features.document_loader import load_document

# -------------------
# Setup
# -------------------
setup_page()
render_title()

# -------------------
# Sidebar
# -------------------
agent_mode = st.sidebar.checkbox("Agent Mode", value=False)

selected_mode = st.sidebar.selectbox("Mode", list(MODES.keys()))
selected_model_label = st.sidebar.selectbox("Model", list(MODEL_OPTIONS.keys()))
selected_model = MODEL_OPTIONS[selected_model_label]
temperature = st.sidebar.slider("Temperature", 0.0, 1.5, 0.7)

# -------------------
# Bot Init
# -------------------
if "bot" not in st.session_state:
    st.session_state.bot = ChatbotAI(
        model=selected_model,
        system_prompt=MODES[selected_mode]
    )

bot = st.session_state.bot

# -------------------
# Chat
# -------------------
if prompt := st.chat_input("Type your message..."):
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        placeholder = st.empty()
        full_text = ""

        gen = bot.chat(prompt, temperature)

        for partial in gen:
            full_text = partial
            placeholder.markdown(full_text + "▌")

        placeholder.empty()
        render_response(full_text)
