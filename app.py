import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="CSRL Colombia - Dashboard", layout="wide")

# Encabezado con tu marca
st.title("🏎️ CSRL Colombia: Sim Racing League")
st.markdown("### Clasificación Oficial y Estadísticas")

# Cargar los datos desde tu GitHub (usa tus nombres de archivo)
@st.cache_data
def load_data():
    # Reemplaza 'TU_USUARIO' por tu nombre de cuenta de GitHub
    url = "https://raw.githubusercontent.com/TU_USUARIO/csrl-liga/main/F1LM.v1.41.4.xlsx%20-%20Final%20Classifications.csv"
    df = pd.read_csv(url)
    return df

try:
    data = load_data()
    
    # Mostrar la tabla de posiciones
    st.subheader("🏆 Tabla de Pilotos")
    st.dataframe(data.style.highlight_max(axis=0, color='#FFD700'), use_container_width=True)

    # Gráfico de puntos
    st.subheader("📊 Rendimiento por Piloto")
    st.bar_chart(data.set_index('Name')['Points'])

except Exception as e:
    st.error("Todavía estamos calentando motores. Asegúrate de que los archivos CSV estén en el repositorio.")
