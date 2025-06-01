import streamlit as st
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

def show_analysis_page(show_full=True):
    # Заголовок с иконкой
    st.markdown("""
    <div style="display:flex;align-items:center;gap:15px">
        <h1 style="margin:0">📈 Equipment Analytics</h1>
    </div>
    """, unsafe_allow_html=True)
    
    # Карточки метрик в сетке
    if show_full:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("""
            <div class="metric-card">
                <div style="display:flex;align-items:center;gap:10px">
                    <div style="font-size:24px">📊</div>
                    <div>
                        <h3 style="margin:0">Model Accuracy</h3>
                        <h1 style="margin:0;color:#5e72e4">96.2%</h1>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Аналогично для col2 и col3

    # Интерактивный 3D график
    st.markdown("### 🎚️ Equipment Status Overview")
    fig = px.scatter_3d(
        get_equipment_data(),
        x='temperature',
        y='vibration',
        z='rpm',
        color='status',
        hover_name='equipment_id',
        size='wear',
        size_max=18
    )
    st.plotly_chart(fig, use_container_width=True)

    # Форма прогнозирования
    with st.expander("🔮 Predict Failure Risk", expanded=True):
        with st.form("prediction_form"):
            cols = st.columns([1,1,2])
            with cols[0]:
                equip_type = st.selectbox("Type", ["L", "M", "H"])
                temp = st.slider("Temperature", 250, 400, 300)
            with cols[1]:
                vibration = st.number_input("Vibration", 0.0, 10.0, 2.5)
                rpm = st.number_input("RPM", 0, 5000, 1500)
            
            if st.form_submit_button("Calculate Risk", use_container_width=True):
                risk = calculate_risk(temp, vibration, rpm)
                st.success(f"Risk level: {risk:.1%}")

def get_equipment_data():
    # Загрузка данных (заглушка)
    return pd.DataFrame({
        'equipment_id': ['EQ-001', 'EQ-002', 'EQ-003'],
        'temperature': [320, 295, 350],
        'vibration': [2.1, 4.5, 1.8],
        'rpm': [1450, 2100, 1800],
        'wear': [120, 240, 80],
        'status': ['Normal', 'Warning', 'Critical']
    })

def calculate_risk(temp, vibration, rpm):
    # Логика прогнозирования (заглушка)
    return min(0.95, (temp-250)/200 * (vibration/5) * (rpm/3000))