"""Main Streamlit entry point."""

import os
import sys

import streamlit as st

sys.path.insert(0, os.path.dirname(__file__))

from backend.config import AppConfig
from backend.engine import EngineFacade
from frontend.dashboard import DashboardRenderer
from frontend.sidebar import SidebarController
from frontend.styles import GLOBAL_CSS


def configure_page() -> None:
    config = AppConfig()
    st.set_page_config(
        page_title=config.page_title,
        page_icon=config.page_icon,
        layout=config.layout,
        initial_sidebar_state=config.sidebar_state,
    )


def initialize_state():
    if "engine" not in st.session_state:
        st.session_state["engine"] = EngineFacade.create_state()
    return st.session_state["engine"]


def main() -> None:
    configure_page()
    st.markdown(GLOBAL_CSS, unsafe_allow_html=True)
    engine_state = initialize_state()
    SidebarController(engine_state).render()
    DashboardRenderer(engine_state).render()


if __name__ == "__main__":
    main()
