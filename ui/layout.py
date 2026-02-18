# ui/layout.py
import streamlit as st
from style import style

def setup_page():
    st.set_page_config(
        page_title="My AI Assistant By Taein Kim",
        page_icon="🤖"
    )
    st.markdown(style, unsafe_allow_html=True)

def render_title():
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
