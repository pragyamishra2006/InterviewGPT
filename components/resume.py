"""Resume analysis experience for generating tailored interview questions."""

from __future__ import annotations

import os

import streamlit as st


def render_resume_page() -> None:
    """Render the resume analysis flow."""
    st.markdown("## 📄 Resume Intelligence")
    st.caption(
        "Upload a resume to generate project-based, HR, and technical "
        "questions"
    )

    uploaded_resume = st.file_uploader(
        "Upload resume",
        type=["pdf", "docx", "txt"],
        key="resume_uploader",
    )
    if uploaded_resume:
        save_path = os.path.join("uploads", uploaded_resume.name)
        with open(save_path, "wb") as handle:
            handle.write(uploaded_resume.getbuffer())
        st.success(f"Resume uploaded: {uploaded_resume.name}")

    if st.button("Analyze Resume", use_container_width=True):
        st.info(
            "Resume-based interview questions and feedback are ready for "
            "expansion with your preferred parsing backend."
        )
        st.markdown("### Suggested Questions")
        st.write("- Project-based: Describe a feature you built end-to-end.")
        st.write("- HR: Why do you want to work at this company?")
        st.write(
            "- Behavioral: Tell me about a time you worked under pressure."
        )
        st.write("- Technical: Explain a system design trade-off you made.")
        st.markdown("### Strengths")
        st.write("- Strong ownership and communication")
        st.markdown("### Weaknesses")
        st.write("- Can improve on depth for trade-off discussions")
        st.markdown("### Interview Tips")
        st.write("- Use STAR format for behavioral stories")
