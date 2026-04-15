# File: IntelleX/dashboard/leaderboard.py

import streamlit as st
import pandas as pd
from utils.db import get_leaderboard

def leaderboard_page():
    st.title("🏆 Leaderboard")

    data = get_leaderboard()

    df = pd.DataFrame(
        data,
        columns=["Email", "Score", "Modules", "Streak"]
    )

    st.dataframe(df, use_container_width=True)