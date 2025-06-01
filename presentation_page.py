import streamlit as st

def show_presentation_page():
    # Кастомный заголовок
    st.markdown("""
    <div style="background:linear-gradient(90deg, #1e2130, #0e1117);
                padding:20px;
                border-radius:10px;
                margin-bottom:30px">
        <h1 style="color:white;margin:0">📊 Project Presentation</h1>
    </div>
    """, unsafe_allow_html=True)
    
    # Карточки с информацией
    cols = st.columns(2)
    with cols[0]:
        with st.container(border=True):
            st.markdown("### 🎯 Project Goals")
            st.markdown("""
            - Predict equipment failures before they occur
            - Reduce maintenance costs by 20-30%
            - Improve equipment lifespan
            """)
    
    with cols[1]:
        with st.container(border=True):
            st.markdown("### ⚙️ Technologies Used")
            st.markdown("""
            - Python 3.10
            - Streamlit
            - Plotly
            - XGBoost
            """)
    
    # Горизонтальный разделитель
    st.divider()
    
    # Временная шкала проекта
    st.markdown("### 📅 Project Timeline")
    with st.expander("View Development Stages"):
        st.markdown("""
        1. **Data Collection** (2 weeks)
        2. **Model Development** (3 weeks)
        3. **UI Design** (1 week)
        4. **Testing** (2 weeks)
        """)