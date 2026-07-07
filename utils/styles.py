"""Helpers for loading and applying the app's custom stylesheet."""

from __future__ import annotations

from pathlib import Path

import streamlit as st


def load_css(theme: str = "dark") -> str:
    """Load the custom CSS stylesheet and adapt colors to the current theme."""
    css_path = Path("styles/style.css")
    css = css_path.read_text(encoding="utf-8")
    if theme != "dark":
        css = css.replace("#0b1020", "#f5f7ff")
        css = css.replace("#111827", "#ffffff")
        css = css.replace("#1f2937", "#eef2ff")
        css = css.replace("rgba(255,255,255,0.08)", "rgba(15,23,42,0.06)")
        css = css.replace("rgba(255,255,255,0.12)", "rgba(15,23,42,0.1)")
        css = css.replace("rgba(255,255,255,0.06)", "rgba(15,23,42,0.05)")
        css = css.replace("#4da3ff", "#2563eb")
        css = css.replace("#7c3aed", "#7c3aed")
        css = css.replace("#22d3ee", "#0891b2")
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
