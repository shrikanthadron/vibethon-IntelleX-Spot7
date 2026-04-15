# File: IntelleX/dashboard/progress.py

import streamlit as st
import plotly.express as px
from utils.db import get_progress

def progress_page():
    st.title("📊 Progress Dashboard")

    if not st.session_state.get("logged_in"):
        st.warning("Please login first.")
        return

    row = get_progress(st.session_state.user_id)

    if row:
        modules, score, streak, _ = row

        c1, c2, c3 = st.columns(3)
        c1.metric("📚 Modules", modules)
        c2.metric("🏆 Score", score)
        c3.metric("🔥 Streak", streak)

        progress = min(modules / 3, 1.0)
        st.progress(progress)

        fig = px.bar(
            x=["Modules", "Score", "Streak"],
            y=[modules, score, streak],
            title="Performance Overview"
        )
        st.plotly_chart(fig, use_container_width=True)