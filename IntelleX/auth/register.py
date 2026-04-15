import streamlit as st
import sqlite3
from utils.db import create_user, get_user_by_email
from auth.utils import hash_password, valid_email, strong_password

def register_page():
    st.title("📝 Register")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm = st.text_input("Confirm Password", type="password")

    if st.button("Create Account"):

        if not valid_email(email):
            st.error("Invalid email")
            return

        if not strong_password(password):
            st.error("Weak password")
            return

        if password != confirm:
            st.error("Passwords do not match")
            return

        if get_user_by_email(email):
            st.warning("Email already exists. Please login.")
            return

        try:
            hashed = hash_password(password)
            create_user(email, hashed)
            st.success("Account created successfully!")
        except sqlite3.IntegrityError:
            st.warning("Email already registered.")