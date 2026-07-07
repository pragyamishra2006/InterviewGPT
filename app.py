"""Main Streamlit entry point for the redesigned InterviewGPT experience."""

from __future__ import annotations

import os

import streamlit as st

from components.chat import init_session_defaults, render_chat_page
from components.dashboard import render_home_dashboard
from components.mock_interview import render_mock_interview_page
from components.resume import render_resume_page
from components.settings import render_settings_page
from components.sidebar import render_sidebar
from components.upload import render_upload_page
from utils.styles import load_css


st.set_page_config(page_title="InterviewGPT", page_icon="🤖", layout="wide")

init_session_defaults()
os.makedirs("uploads", exist_ok=True)

load_css(st.session_state.theme)

render_sidebar()

st.markdown(
    """
    <div class="topbar-shell">
        <div class="topbar-left">
            <div class="topbar-brand">InterviewGPT</div>
            <div class="topbar-subtitle">AI-powered job prep workspace</div>
        </div>
        <div class="topbar-right">
            <div class="topbar-search">🔎 Search chats, notes, and prompts</div>
            <div class="topbar-pill">🔔 3</div>
            <div class="topbar-pill">☾</div>
            <div class="avatar-pill">AI</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

page = st.session_state.page
if page == "Home":
    render_home_dashboard()
elif page == "Chat":
    render_chat_page()
elif page == "Upload":
    render_upload_page()
elif page == "Mock Interview":
    render_mock_interview_page()
elif page == "Resume":
    render_resume_page()
elif page == "Settings":
    render_settings_page()

st.markdown("---")
st.caption(
    "Built with Streamlit, LangChain, ChromaDB, Ollama, and Hugging "
    "Face embeddings."
)
