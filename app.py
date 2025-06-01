import streamlit as st
from streamlit_option_menu import option_menu
from analysis_page import show_analysis_page
from presentation_page import show_presentation_page

st.set_page_config(page_title="Predictive Maintenance", layout="wide")

with st.sidebar:
    selected = option_menu(
        "Main Menu",
        ["Data Analysis & Model", "Project Presentation"],
        icons=["clipboard-data", "easel"],
        default_index=0,
    )

if selected == "Data Analysis & Model":
    show_analysis_page()
elif selected == "Project Presentation":
    show_presentation_page()