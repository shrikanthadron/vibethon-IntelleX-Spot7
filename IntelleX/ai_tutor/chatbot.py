# File: IntelleX/ai_tutor/chatbot.py

import streamlit as st
from groq import Groq
from gtts import gTTS
import tempfile
import os

# ---------------- CLIENT ----------------
def get_client():
    try:
        return Groq(api_key="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")
    except:
        return None

# ---------------- PROMPT ----------------
SYSTEM_PROMPT = """
You are IntelleX AI Tutor.

Always answer in this format:
1. Simple Explanation
2. Technical Explanation
3. Real-world Example
4. Key Points
5. Short Summary

Be detailed, educational, beginner-friendly, and accurate.
If user asks coding, provide code examples.
If user asks concepts, explain deeply.
"""

# ---------------- TTS ----------------
def speak_text(text):
    tts = gTTS(text=text, lang="en")
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(tmp.name)

    with open(tmp.name, "rb") as f:
        audio_bytes = f.read()

    st.audio(audio_bytes, format="audio/mp3")
    os.unlink(tmp.name)

# ---------------- PAGE ----------------
def ai_tutor_page():
    st.title("🤖 IntelleX AI Tutor")
    st.caption("Deep Explanations + Voice Learning")

    client = get_client()

    if client is None:
        st.error("Groq API key missing.")
        return

    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "last_reply" not in st.session_state:
        st.session_state.last_reply = ""

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    prompt = st.chat_input("Ask any AIML doubt...")

    if prompt:
        st.session_state.messages.append(
            {"role": "user", "content": prompt}
        )

        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Generating detailed explanation..."):

                msgs = [{"role": "system", "content": SYSTEM_PROMPT}]
                msgs.extend(st.session_state.messages)

                response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=msgs,
    temperature=0.3,
    max_tokens=1200
)

                reply = response.choices[0].message.content
                st.markdown(reply)

        st.session_state.messages.append(
            {"role": "assistant", "content": reply}
        )
        st.session_state.last_reply = reply

    st.sidebar.subheader("🎙 Voice Learning")

    if st.sidebar.button("🔊 Speak Last Answer"):
        if st.session_state.last_reply:
            speak_text(st.session_state.last_reply)
        else:
            st.sidebar.warning("No answer yet.")

    if st.sidebar.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.session_state.last_reply = ""
        st.rerun()