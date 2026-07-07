"""Home dashboard, analytics cards, and launchpad experience."""

from __future__ import annotations

import os

import streamlit as st

from components.cards import feature_card, quick_action_card, stat_card


def render_home_dashboard() -> None:
    """Render the premium home landing experience."""
    st.markdown(
        """
        <div class="hero-shell">
            <div class="hero-badge">🚀 Crack Your Dream Job with AI</div>
            <div class="hero-title">Resume Intelligence • AI Chat • Mock Interviews • RAG Knowledge Base</div>
            <div class="hero-subtitle">A polished interview operating system designed for modern candidates and hackathon-ready demos.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns([1.1, 1, 1])
    with c1:
        if st.button("Upload Resume", use_container_width=True):
            st.session_state.page = "Upload"
    with c2:
        if st.button("Start Mock Interview", use_container_width=True):
            st.session_state.page = "Mock Interview"
    with c3:
        if st.button("Ask AI", use_container_width=True):
            st.session_state.page = "Chat"

    st.markdown("### ✨ Core Workspace Modules")
    feature_columns = st.columns(3)
    features = [
        ("Resume Analysis", "Get instant feedback and tailored interview prep from your resume.", "📄", "Resume", "Resume"),
        ("AI Chat", "Ask grounded questions and keep every answer tied to your knowledge base.", "💬", "Chat", "Chat"),
        ("Mock Interview", "Practice realistic rounds with smart prompts and scoring guidance.", "🎤", "Practice", "Mock Interview"),
        ("Knowledge Base", "Turn notes and PDFs into a searchable retrieval layer for stronger answers.", "🧠", "Explore", "Upload"),
        ("Interview History", "Review every session and keep momentum across your prep journey.", "🗂️", "Open", "Chat"),
        ("Career Insights", "Track readiness and focus on the areas that need attention most.", "📈", "Review", "Settings"),
    ]
    for index, feature in enumerate(features):
        with feature_columns[index % 3]:
            feature_card(*feature)

    st.markdown("### 📊 Live Performance Pulse")
    stat_columns = st.columns(3)
    with stat_columns[0]:
        stat_card("Resume Score", "88 / 100", "🎯", "+6% this week")
    with stat_columns[1]:
        stat_card("Questions Answered", "124", "❓", "12 today")
    with stat_columns[2]:
        stat_card("Mock Interviews", "9", "🎤", "3 completed this week")

    stat_columns_2 = st.columns(3)
    with stat_columns_2[0]:
        stat_card("Documents Uploaded", "4", "📦", "2 PDFs ready")
    with stat_columns_2[1]:
        stat_card("AI Responses", "81", "⚡", "Fast and grounded")
    with stat_columns_2[2]:
        stat_card("Interview Readiness", "92%", "🏁", "On pace")

    st.markdown("### 🧩 AI Pipeline")
    pipeline_items = [
        ("Upload Resume", "📄"),
        ("PDF Processing", "🧾"),
        ("Chunking", "✂️"),
        ("Embeddings", "🧠"),
        ("Vector Database", "🗄️"),
        ("Retriever", "🔎"),
        ("LLM", "⚙️"),
        ("Final AI Response", "✨"),
    ]
    pipeline_html = "<div class='pipeline-row'>"
    for label, icon in pipeline_items:
        pipeline_html += f"<div class='pipeline-stage'><div class='pipeline-icon'>{icon}</div><div>{label}</div></div>"
    pipeline_html += "</div>"
    st.markdown(f"<div class='panel-card'>{pipeline_html}</div>", unsafe_allow_html=True)

    st.markdown("### 🌀 Readiness Radar")
    progress_columns = st.columns(3)
    progress_items = [
        ("Resume Score", 88, "#3b82f6"),
        ("Communication", 82, "#06b6d4"),
        ("Technical Skills", 91, "#8b5cf6"),
        ("Confidence", 79, "#22c55e"),
        ("Behavioral", 84, "#f59e0b"),
        ("Problem Solving", 87, "#ec4899"),
    ]
    for index, (label, value, color) in enumerate(progress_items):
        with progress_columns[index % 3]:
            st.markdown(
                f"<div class='progress-card'><div class='progress-ring' style='--progress:{value}; --accent:{color};'><span>{value}%</span></div><div class='progress-label'>{label}</div></div>",
                unsafe_allow_html=True,
            )

    st.markdown("### 🕒 Recent Activity")
    activity_items = [
        ("Uploaded Resume", "2 mins ago"),
        ("Started Interview", "18 mins ago"),
        ("Asked AI Question", "41 mins ago"),
        ("Generated Resume Feedback", "1 hr ago"),
    ]
    activity_html = "<div class='timeline-card'>"
    for title, time_text in activity_items:
        activity_html += f"<div class='timeline-item'><div class='timeline-dot'></div><div><div class='timeline-title'>{title}</div><div class='timeline-time'>{time_text}</div></div></div>"
    activity_html += "</div>"
    st.markdown(activity_html, unsafe_allow_html=True)

    st.markdown("### ⚡ Quick Actions")
    action_columns = st.columns(5)
    actions = [
        ("+ Upload PDF", "Upload", "📤"),
        ("+ Upload Resume", "Upload", "📄"),
        ("+ New Chat", "Chat", "💬"),
        ("+ Mock Interview", "Mock Interview", "🎤"),
        ("+ Resume Review", "Resume", "📝"),
    ]
    for index, (label, target, icon) in enumerate(actions):
        with action_columns[index]:
            if st.button(f"{icon} {label}", use_container_width=True):
                st.session_state.page = target

    st.markdown("### 📈 Insight Dashboard")
    chart_cols = st.columns(2)
    with chart_cols[0]:
        st.markdown("<div class='panel-card'><div class='panel-title'>Weekly Interview Progress</div></div>", unsafe_allow_html=True)
        st.line_chart([3, 5, 4, 6, 7, 8, 9], height=220)
    with chart_cols[1]:
        st.markdown("<div class='panel-card'><div class='panel-title'>Questions by Topic</div></div>", unsafe_allow_html=True)
        st.bar_chart({"DSA": 8, "OS": 5, "DBMS": 6, "Behavioral": 4}, height=220)

    st.markdown("### 🧠 RAG Intelligence")
    rag_columns = st.columns(2)
    with rag_columns[0]:
        stat_card("Knowledge Base", "4 PDFs", "🗂️", "Indexed and searchable")
        stat_card("Chunks Indexed", "120", "🧩", "Optimized retrieval")
    with rag_columns[1]:
        stat_card("Embedding Model", "nomic-embed-text", "🧬", "Local embeddings")
        stat_card("Retrieved Sources", "7", "🔗", "Relevant context")

    st.markdown("### 🔗 Quick Navigation")
    nav_columns = st.columns(4)
    with nav_columns[0]:
        quick_action_card("Resume Review", "Open your resume workspace", "📄", "Resume")
    with nav_columns[1]:
        quick_action_card("New Chat", "Continue the conversation", "💬", "Chat")
    with nav_columns[2]:
        quick_action_card("Knowledge Base", "Manage uploaded PDFs", "🧠", "Upload")
    with nav_columns[3]:
        quick_action_card("Workspace Settings", "Tune model and retrieval", "⚙️", "Settings")
