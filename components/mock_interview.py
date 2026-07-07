"""Mock interview experience with topic, difficulty, timer, and evaluation."""

from __future__ import annotations

import streamlit as st


def render_mock_interview_page() -> None:
    """Render the interview practice experience."""
    st.markdown("## 🎤 Mock Interview Studio")
    st.caption("Practice technical and behavioral rounds with feedback")

    topic = st.selectbox(
        "Topic",
        [
            "DSA",
            "Operating Systems",
            "DBMS",
            "Computer Networks",
            "OOP",
            "System Design",
            "Behavioral",
            "Resume Based",
        ],
    )
    difficulty = st.selectbox("Difficulty", ["Easy", "Medium", "Hard"])
    timer = st.slider("Timer (minutes)", 5, 20, 10)

    if st.button("Generate Interview Prompt", use_container_width=True):
        prompt_map = {
            "DSA": (
                "Explain the time complexity of binary search and compare "
                "it with linear search."
            ),
            "Operating Systems": (
                "Describe how deadlocks occur and how they can be prevented."
            ),
            "DBMS": "Discuss ACID properties with a real-world example.",
            "Computer Networks": (
                "Compare TCP and UDP in terms of reliability and latency."
            ),
            "OOP": (
                "Explain the difference between abstraction and "
                "encapsulation."
            ),
            "System Design": (
                "Design a URL shortener service with scalability "
                "considerations."
            ),
            "Behavioral": (
                "Tell me about a time you handled a difficult teammate "
                "situation."
            ),
            "Resume Based": (
                "Walk me through one project from your resume and explain "
                "your contribution."
            ),
        }
        st.session_state.interview_prompt = prompt_map[topic]
        st.session_state.interview_topic = topic
        st.session_state.interview_difficulty = difficulty
        st.session_state.interview_timer = timer

    if st.session_state.get("interview_prompt"):
        st.info(
            f"Topic: {st.session_state.interview_topic} • Difficulty: "
            f"{st.session_state.interview_difficulty}"
        )
        st.markdown(f"**Prompt:** {st.session_state.interview_prompt}")
        st.text_area(
            "Your answer",
            height=180,
            placeholder="Record your response here",
        )
        if st.button("Evaluate", use_container_width=True):
            st.success(
                "Evaluation ready. Score and feedback can be connected to "
                "your preferred LLM backend."
            )
            st.metric("Score", "8.5/10")
            st.markdown(
                "**Feedback:** Clear structure, strong examples, and a "
                "little more depth on trade-offs."
            )
            st.markdown(
                "**Ideal Answer:** Focus on the core concept, mention "
                "complexity, and include a short example."
            )
