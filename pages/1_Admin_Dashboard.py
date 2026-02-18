import streamlit as st

st.set_page_config(page_title="Admin Dashboard", page_icon="📊")

st.title("📊 AI Admin Dashboard")

if "bot" not in st.session_state:
    st.warning("No active AI session.")
    st.stop()

bot = st.session_state.bot

st.subheader("Model Info")
st.write("Model:", bot.model)

st.divider()

st.subheader("Usage Stats")

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Tokens Used", bot.total_tokens)

with col2:
    st.metric("Total Cost ($)", f"{bot.total_cost:.6f}")

st.divider()

st.subheader("Last Request Usage")

if bot.last_usage:
    st.write("Prompt Tokens:", bot.last_usage.get("prompt_tokens"))
    st.write("Completion Tokens:", bot.last_usage.get("completion_tokens"))
    st.write("Total Tokens:", bot.last_usage.get("total_tokens"))
else:
    st.info("No request yet.")

st.divider()

st.subheader("Conversation Info")
st.write("Messages in Memory:", len(bot.messages))
