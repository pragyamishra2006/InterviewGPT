"""Reusable cards and stat surfaces for the premium dashboard UI."""

from __future__ import annotations

import streamlit as st


def stat_card(title: str, value: str, icon: str = "✦", detail: str = "") -> None:
    """Render a polished analytics card."""
    detail_html = f'<div class="stat-card-detail">{detail}</div>' if detail else ""
    st.markdown(
        f"""
        <div class="stat-card">
            <div class="stat-card-icon">{icon}</div>
            <div class="stat-card-body">
                <div class="stat-card-title">{title}</div>
                <div class="stat-card-value">{value}</div>
                {detail_html}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def quick_action_card(
    title: str,
    description: str,
    icon: str,
    page: str,
) -> None:
    """Render a premium quick-action tile."""
    st.markdown("<div class='quick-card'>", unsafe_allow_html=True)
    if st.button(
        f"{icon} {title}",
        key=f"quick_{title.lower().replace(' ', '_')}",
        use_container_width=True,
    ):
        st.session_state.page = page
    st.caption(description)
    st.markdown("</div>", unsafe_allow_html=True)


def feature_card(
    title: str,
    description: str,
    icon: str,
    action_label: str,
    page: str,
    accent: str = "#3b82f6",
) -> None:
    """Render a premium feature card with a call to action."""
    st.markdown(
        f"""
        <div class="feature-card" style="--accent:{accent};">
            <div class="feature-card-icon">{icon}</div>
            <div class="feature-card-title">{title}</div>
            <div class="feature-card-description">{description}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button(action_label, key=f"feature_{title.lower().replace(' ', '_')}", use_container_width=True):
        st.session_state.page = page
