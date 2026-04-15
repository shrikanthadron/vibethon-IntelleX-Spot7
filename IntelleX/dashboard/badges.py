# File: IntelleX/dashboard/badges.py

import streamlit as st
from utils.db import get_progress

def badges_page():
    st.title("🎖️ Badges")

    if not st.session_state.get("logged_in"):
        st.warning("Please login first.")
        return

    row = get_progress(st.session_state.user_id)

    if row:
        modules, score, streak, _ = row

        badges = []

        if score >= 20:
            badges.append("🥉 Bronze Learner")
        if score >= 50:
            badges.append("🥈 Silver Learner")
        if score >= 100:
            badges.append("🥇 Gold Learner")
        if modules >= 3:
            badges.append("🚀 Module Master")
        if streak >= 5:
            badges.append("🔥 Consistency Star")

        if badges:
            for badge in badges:
                st.success(badge)
        else:
            st.info("No badges unlocked yet.")