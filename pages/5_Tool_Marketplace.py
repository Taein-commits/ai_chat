import streamlit as st

st.set_page_config(page_title="Tool Marketplace", page_icon="🛒")

st.title("🛒 Tool Marketplace")

if "bot" not in st.session_state:
    st.warning("No active AI session.")
    st.stop()

bot = st.session_state.bot
registry = bot.tool_registry

st.subheader("Available Tools")

for name, info in registry.tools.items():

    col1, col2, col3 = st.columns([3,2,2])

    with col1:
        st.write(name)

    with col2:
        enabled = st.checkbox(
            "Enabled",
            value=info["enabled"],
            key=name
        )

        if enabled:
            registry.enable(name)
        else:
            registry.disable(name)

    with col3:
        st.write(f"Usage: {info['usage']}")
