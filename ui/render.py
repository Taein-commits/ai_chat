# ui/render.py
import streamlit as st
import re

def render_response(text: str) -> None:
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
