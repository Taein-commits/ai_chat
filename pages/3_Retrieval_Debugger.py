import streamlit as st

st.set_page_config(page_title="Retrieval Debugger", page_icon="🔎")

st.title("🔎 Retrieval Debugger")

if "bot" not in st.session_state:
    st.warning("No active AI session.")
    st.stop()

bot = st.session_state.bot

if not hasattr(bot, "last_retrieval") or not bot.last_retrieval:
    st.info("No retrieval data yet. Ask a question first.")
    st.stop()

st.subheader("Top Retrieved Memories")

for i, (content, score) in enumerate(bot.last_retrieval, start=1):

    with st.expander(f"Rank {i} — Similarity: {score:.4f}"):

        st.write(content[:1500])

        if i == 1:
            st.success("⬆ This memory was most relevant")
