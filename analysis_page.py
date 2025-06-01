import streamlit as st
import pandas as pd
import plotly.express as px
from io import StringIO

# Константы
DEFAULT_DATA = """equipment_id,temperature,vibration,rpm,wear,status
EQ-001,320,2.1,1450,120,Normal
EQ-002,295,4.5,2100,240,Warning
EQ-003,350,1.8,1800,80,Critical
EQ-004,310,3.2,1950,150,Normal
EQ-005,280,5.1,2250,210,Warning"""

def load_default_data():
    """Загружает демо-данные по умолчанию"""
    return pd.read_csv(StringIO(DEFAULT_DATA))

def validate_data(data):
    """Проверяет структуру данных"""
    required_columns = {'temperature', 'vibration', 'rpm', 'wear', 'status'}
    if not required_columns.issubset(data.columns):
        missing = required_columns - set(data.columns)
        raise ValueError(f"Отсутствуют обязательные колонки: {missing}")
    return data

def process_uploaded_file(uploaded_file):
    """Обрабатывает загруженный файл"""
    try:
        data = pd.read_csv(uploaded_file)
        return validate_data(data)
    except Exception as e:
        st.error(f"Ошибка обработки файла: {str(e)}")
        return None

def render_metrics(data):
    """Отображает ключевые метрики"""
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Всего единиц", len(data))
    with col2:
        st.metric("Критический статус",
                len(data[data['status'] == 'Critical']),
                delta_color="inverse")
    with col3:
        avg_wear = data['wear'].mean()
        st.metric("Средний износ", f"{avg_wear:.1f} мин")

def render_3d_plot(data):
    """Создает 3D визуализацию"""
    fig = px.scatter_3d(
        data,
        x='temperature',
        y='vibration',
        z='rpm',
        color='status',
        size='wear',
        hover_name='equipment_id',
        color_discrete_map={
            'Normal': '#2ecc71',
            'Warning': '#f39c12',
            'Critical': '#e74c3c'
        },
        title="3D Анализ параметров оборудования"
    )
    fig.update_layout(margin=dict(l=0, r=0, b=0, t=30))
    st.plotly_chart(fig, use_container_width=True)

def render_prediction_form():
    """Форма для ручного ввода прогноза"""
    with st.expander("🔮 Ручной прогноз отказа", expanded=True):
        with st.form("prediction_form"):
            cols = st.columns(2)
            with cols[0]:
                temp = st.slider("Температура (K)", 250, 400, 300)
                rpm = st.slider("Обороты (RPM)", 0, 5000, 1500)
            with cols[1]:
                vibration = st.slider("Вибрация (mm/s²)", 0.0, 10.0, 2.5)
                wear = st.slider("Износ (мин)", 0, 300, 50)

            if st.form_submit_button("Рассчитать риск"):
                risk = min(0.95, (temp-250)/200 * (vibration/5) * (rpm/3000) * (wear/200))
                st.progress(risk)
                if risk > 0.7:
                    st.error(f"Высокий риск отказа: {risk:.1%}")
                elif risk > 0.4:
                    st.warning(f"Средний риск: {risk:.1%}")
                else:
                    st.success(f"Низкий риск: {risk:.1%}")

def show_analysis_page():
    """Основная функция страницы анализа"""
    st.title("📊 Анализ состояния оборудования")

    # Загрузка данных
    uploaded_file = st.file_uploader(
        "Загрузите CSV файл с данными оборудования",
        type=["csv"],
        help="Файл должен содержать колонки: temperature, vibration, rpm, wear, status"
    )

    data = process_uploaded_file(uploaded_file) if uploaded_file else load_default_data()

    if data is not None:
        # Основная информация
        st.info(f"Загружено {len(data)} записей | Источник: {'ваш файл' if uploaded_file else 'демо-данные'}")

        # Визуализации
        render_metrics(data)
        render_3d_plot(data)

        # Дополнительные функции
        with st.expander("📄 Просмотр данных"):
            st.dataframe(data)

        render_prediction_form()
    else:
        st.warning("Используются демонстрационные данные")
        data = load_default_data()
        render_3d_plot(data)