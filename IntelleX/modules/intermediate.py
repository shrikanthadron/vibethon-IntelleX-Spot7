# File: IntelleX/modules/intermediate.py

import streamlit as st
import json
from utils.db import complete_module, add_score

def intermediate_page():
    st.title("📙 Intermediate Module")

    with open("modules/content.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    lessons = data["intermediate"]

    for i, lesson in enumerate(lessons, start=1):
        with st.expander(f"Lesson {i}: {lesson['title']}", expanded=True):
            st.write(lesson["content"])
            st.info(lesson["example"])

    if st.button("✅ Complete Intermediate Module"):
        if st.session_state.get("logged_in"):
            complete_module(st.session_state.user_id)
            add_score(st.session_state.user_id, 20)
            st.success("Completed! +20 XP")
        else:
            st.warning("Please login first.")