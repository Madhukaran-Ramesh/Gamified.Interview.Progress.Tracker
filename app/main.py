import streamlit as st
import streamlit_authenticator as stauth
import plotly.graph_objects as go
import pandas as pd
from backend.auth import authenticate_user, register_user, get_user_progress, update_progress, get_leaderboard
from backend.missions import get_missions
from models.db import create_db
import os

# Initialize DB
if not os.path.exists(os.path.join(os.path.dirname(__file__), '../gamified_interview.db')):
    create_db()

st.set_page_config(page_title="Gamified Interview Tracker", page_icon="🎮", layout="wide")
st.title("🎮 Gamified Interview Progress Tracker")

# --- Authentication ---
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

menu = ["Login", "Register"] if not st.session_state['authenticated'] else ["Dashboard", "Missions", "Leaderboard", "Logout"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Register":
    st.subheader("Register")
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Register"):
        success, msg = register_user(username, password, email)
        st.success(msg) if success else st.error(msg)
elif choice == "Login":
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        user = authenticate_user(username, password)
        if user:
            st.session_state['authenticated'] = True
            st.session_state['user'] = user
            st.experimental_rerun()
        else:
            st.error("Invalid credentials.")

# --- Main App ---
if st.session_state.get('authenticated', False):
    user = st.session_state['user']
    if choice == "Dashboard":
        st.header(f"Welcome, {user.username}!")
        progress = get_user_progress(user.id)
        # Progress Bar
        st.subheader("Your Progress")
        st.progress(min(progress.stage * 20, 100))
        # Badges
        st.subheader("Badges")
        badges = progress.achievements.split(',') if progress.achievements else []
        st.write(", ".join(badges) if badges else "No badges yet.")
        # Score
        st.metric("Score", user.score)
        # Achievements
        st.subheader("Achievements")
        st.write(progress.achievements if progress.achievements else "No achievements yet.")
        # Plotly Chart
        fig = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = user.score,
            title = {'text': "Total Score"},
            gauge = {'axis': {'range': [None, 1000]}}
        ))
        st.plotly_chart(fig, use_container_width=True)
    elif choice == "Missions":
        progress = get_user_progress(user.id)
        st.header(f"Stage {progress.stage} - Level {progress.level}")
        missions = get_missions(progress.stage, progress.level)
        for m in missions:
            st.subheader(m.name)
            st.write(m.description)
            if m.is_timed:
                st.info(f"Timed Challenge: {m.time_limit} seconds")
            if st.button(f"Start {m.name}"):
                st.success(f"Mission '{m.name}' started!")
                # Here, add logic for mission/hurdle UI and completion
    elif choice == "Leaderboard":
        st.header("Leaderboard")
        leaderboard = get_leaderboard()
        df = pd.DataFrame([{ 'Username': u.username, 'Score': u.score } for u in leaderboard])
        st.dataframe(df)
    elif choice == "Logout":
        st.session_state['authenticated'] = False
        st.session_state['user'] = None
        st.success("Logged out.")
        st.experimental_rerun()
