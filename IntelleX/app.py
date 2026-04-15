import streamlit as st
from utils.db import init_db
from auth.login import login_page, logout_button
from auth.register import register_page
from modules.beginner import beginner_page
from modules.intermediate import intermediate_page
from modules.advanced import advanced_page
from quizzes.beginner_quiz import beginner_quiz_page
from quizzes.intermediate_quiz import intermediate_quiz_page
from quizzes.advanced_quiz import advanced_quiz_page
from simulations.spam_detection import spam_detection_page
from simulations.image_classifier import image_classifier_page
from dashboard.progress import progress_page
from dashboard.leaderboard import leaderboard_page
from dashboard.badges import badges_page
from ai_tutor.chatbot import ai_tutor_page
st.set_page_config(page_title='IntelleX Futuristic', page_icon='🤖', layout='wide', initial_sidebar_state='expanded')
init_db()
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

st.markdown('''
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
html, body, [class*="css"] {font-family: 'Orbitron', sans-serif; color: white;}
.stApp {
background: radial-gradient(circle at top left,#0f172a,#111827,#1e1b4b,#000000);
background-size: 400% 400%;
animation: bgMove 12s ease infinite;
}
@keyframes bgMove {0%{background-position:0% 50%;}50%{background-position:100% 50%;}100%{background-position:0% 50%;}}
section[data-testid="stSidebar"] {
background: rgba(17,24,39,0.88);
backdrop-filter: blur(12px);
border-right:1px solid rgba(255,255,255,0.08);
}
.card {
background: rgba(255,255,255,0.07);
border:1px solid rgba(255,255,255,0.08);
padding:20px;
border-radius:22px;
box-shadow:0 8px 30px rgba(0,0,0,0.25);
transition: all .3s ease;
animation: fadeIn .8s ease;
}
.card:hover {transform: translateY(-6px) scale(1.02); box-shadow:0 12px 35px rgba(99,102,241,.35);} 
@keyframes fadeIn {from{opacity:0; transform:translateY(15px);} to{opacity:1; transform:translateY(0);}}
div[data-testid="metric-container"] {background:rgba(255,255,255,0.08); border-radius:18px; padding:12px;}
button[kind="primary"] {border-radius:14px; border:1px solid rgba(255,255,255,.2);} 
</style>
''', unsafe_allow_html=True)

st.sidebar.title('🚀 IntelleX')
st.sidebar.caption('Next-Gen AIML Experience')
if st.session_state.logged_in:
    st.sidebar.success(f"Logged in as {st.session_state.user_email}")
logout_button()
menu = st.sidebar.radio('Navigation',['Home','Login','Register','Learn','Quiz','Simulations','Dashboard','Leaderboard','Badges','AI Tutor'])

if menu == 'Home':
    st.title('🤖 IntelleX Futuristic')
    st.caption('Learn • Build • Compete • Simulate')
    c1,c2,c3 = st.columns(3)
    with c1:
        st.markdown("<div class='card'><h3>📚 Smart Learning</h3><p>Guided AIML pathways with rich lessons.</p></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='card'><h3>🧠 Adaptive Quizzes</h3><p>Instant scoring, XP rewards, progression.</p></div>", unsafe_allow_html=True)
    with c3:
        st.markdown("<div class='card'><h3>🌍 Real Simulations</h3><p>Hands-on demos using ML workflows.</p></div>", unsafe_allow_html=True)
    a,b,c = st.columns(3)
    a.metric('Modules','9+')
    b.metric('XP System','Active')
    c.metric('UI Mode','Futuristic')
    st.info('Use the movable sidebar arrow to collapse/expand navigation anytime.')
elif menu == 'Login':
    login_page()
elif menu == 'Register':
    register_page()
elif menu == 'Learn':
    level = st.selectbox('Choose Level',['Beginner','Intermediate','Advanced'])
    if level=='Beginner': beginner_page()
    elif level=='Intermediate': intermediate_page()
    else: advanced_page()
elif menu == 'Quiz':
    level = st.selectbox('Choose Quiz',['Beginner','Intermediate','Advanced'])
    if level=='Beginner': beginner_quiz_page()
    elif level=='Intermediate': intermediate_quiz_page()
    else: advanced_quiz_page()
elif menu == 'Simulations':
    sim = st.selectbox('Choose Simulation',['Spam Detection','Image Classification'])
    if sim=='Spam Detection': spam_detection_page()
    else: image_classifier_page()
elif menu == 'Dashboard':
    progress_page()
elif menu == 'Leaderboard':
    leaderboard_page()
elif menu == 'Badges':
    badges_page()
elif menu == "AI Tutor":
    ai_tutor_page()