import streamlit as st
from analysis_page import show_analysis_page
from presentation_page import show_presentation_page

# Настройка страницы
st.set_page_config(
    page_title="Smart Equipment Monitor",
    page_icon="⚙️",
    layout="wide"
)

# Стили
st.markdown("""
<style>
    .stMetric { background-color: #1e2130; border-radius: 10px; padding: 15px; }
    .stMetric label { font-size: 0.9rem; color: #a1a9b8 !important; }
    .stMetric h1 { color: #5e72e4 !important; }
</style>
""", unsafe_allow_html=True)

# Навигация
page = st.sidebar.selectbox(
    "Меню",
    ["Анализ оборудования", "Презентация"],
    index=0
)

if page == "Анализ оборудования":
    show_analysis_page()
else:
    show_presentation_page()