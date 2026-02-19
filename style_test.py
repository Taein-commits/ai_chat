import streamlit as st

# Inject your CSS
style = """
<style>

/* Center main container */
.block-container {
    max-width: 800px;
    margin: auto;
    padding-top: 2rem;
}

/* Chat input area glow */
textarea {
    background: #0f172a !important;
    color: white !important;
    border-radius: 20px !important;
    border: 1px solid #334155 !important;
    padding: 12px !important;
}

/* Chat input focus glow */
textarea:focus {
    border: 1px solid #3b82f6 !important;
    box-shadow: 0 0 15px rgba(59,130,246,0.5);
}

/* Smooth chat bubbles */
[data-testid="stChatMessage"] {
    border-radius: 20px;
    padding: 14px 18px;
    animation: fadeIn 0.3s ease-in-out;
}

/* Fade animation */
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(5px);}
    to {opacity: 1; transform: translateY(0);}
}

</style>
"""

st.markdown(style, unsafe_allow_html=True)

st.title("Chat UI Test")

# Fake chat messages
with st.chat_message("assistant"):
    st.write("Hello! This is a test assistant message.")

with st.chat_message("user"):
    st.write("Hi! This is a test user message.")

with st.chat_message("assistant"):
    st.write("Nice glow effect, right?")

# Chat input
user_input = st.chat_input("Type your message...")

if user_input:
    with st.chat_message("user"):
        st.write(user_input)
