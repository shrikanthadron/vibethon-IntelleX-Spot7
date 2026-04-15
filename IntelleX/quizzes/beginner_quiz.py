# File: IntelleX/quizzes/beginner_quiz.py

import streamlit as st
import json
from utils.db import add_score, save_quiz_attempt

def run_quiz(level):
    st.title(f"📝 {level.title()} Quiz")

    with open("quizzes/questions.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    questions = data[level]
    answers = {}

    with st.form(f"{level}_quiz_form"):
        for i, q in enumerate(questions, start=1):
            answers[i] = st.radio(
                f"{i}. {q['question']}",
                q["options"],
                key=f"{level}_{i}"
            )

        submitted = st.form_submit_button("Submit Quiz")

    if submitted:
        score = 0

        for i, q in enumerate(questions, start=1):
            if answers[i] == q["answer"]:
                score += 1

        total = len(questions)
        percent = int((score / total) * 100)

        st.success(f"Score: {score}/{total} ({percent}%)")

        if st.session_state.get("logged_in"):
            xp = score * 10
            add_score(st.session_state.user_id, xp)
            save_quiz_attempt(
                st.session_state.user_id,
                f"{level}_quiz",
                score,
                total
            )
            st.info(f"+{xp} XP added!")

def beginner_quiz_page():
    run_quiz("beginner")