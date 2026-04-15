# File: IntelleX/auth/login.py

import streamlit as st
from datetime import date
from utils.db import get_user_by_email, update_streak
from auth.utils import verify_password

def login_page():
    st.title("🔐 Login")

    with st.form("login_form"):
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")

    if submit:
        user = get_user_by_email(email.strip())

        if not user:
            st.error("User not found.")
            return

        user_id, user_email, password_hash = user

        if verify_password(password, password_hash):
            st.session_state.user_id = user_id
            st.session_state.user_email = user_email
            st.session_state.logged_in = True

            today = str(date.today())
            update_streak(user_id, today)

            st.success("Login successful!")
            st.rerun()
        else:
            st.error("Incorrect password.")


def logout_button():
    if st.session_state.get("logged_in"):
        if st.sidebar.button("Logout"):
            st.session_state.clear()
            st.rerun()