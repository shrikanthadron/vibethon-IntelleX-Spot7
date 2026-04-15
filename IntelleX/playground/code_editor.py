# File: IntelleX/playground/code_editor.py

import streamlit as st

def playground_page():
    st.title("💻 Python Coding Playground")

    sample = '''# Try Python here
for i in range(5):
    print("Hello AIML", i)
'''

    code = st.text_area("Write Code", sample, height=300)

    st.code(code, language="python")

    st.info("For security, this demo shows code only. You can extend with exec() sandbox later.")