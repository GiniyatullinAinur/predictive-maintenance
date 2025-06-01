import streamlit as st
from streamlit_option_menu import option_menu
from analysis_page import show_analysis_page
from presentation_page import show_presentation_page

# Настройка страницы
st.set_page_config(
    page_title="Equipment Health Monitor",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Загрузка кастомных стилей
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Главное меню с анимацией
with st.sidebar:
    st.markdown("""
    <div style="text-align:center;margin-bottom:30px">
        <h1 style="color:#5e72e4;font-size:28px">🛠️ SMART MONITOR</h1>
        <p style="color:#a1a9b8">Predictive Maintenance System</p>
    </div>
    """, unsafe_allow_html=True)
    
    selected = option_menu(
        menu_title=None,
        options=["Dashboard", "Data Analysis", "Presentation"],
        icons=["speedometer", "clipboard-data", "file-earmark-slides"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important"},
            "nav-link": {"font-size": "14px", "margin-bottom": "10px"}
        }
    )

# Роутинг страниц
if selected == "Dashboard":
    show_analysis_page(show_full=True)
elif selected == "Data Analysis":
    show_analysis_page(show_full=False)
elif selected == "Presentation":
    show_presentation_page()