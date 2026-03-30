import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="CSRL Colombia", page_icon="🏎️", layout="wide")

st.title("🏎️ CSRL Colombia Sim Racing")

# Función para cargar tus archivos
def cargar_datos(nombre_archivo):
    # Usamos tu usuario Anthonny2001 que vi en la captura
    user = "Anthonny2001"
    repo = "csrl-liga"
    url = f"https://raw.githubusercontent.com/{user}/{repo}/main/{nombre_archivo.replace(' ', '%20')}"
    return pd.read_csv(url)

try:
    # 1. Tabla de Posiciones
    st.subheader("🏆 Clasificación del Campeonato")
    df_puntos = cargar_datos("F1LM.v1.41.4.xlsx - Final Classifications.csv")
    st.table(df_puntos[['Name', 'Team', 'Points']].head(15))

    # 2. Gráfico de Rendimiento
    st.subheader("📊 Comparativa de Puntos")
    st.bar_chart(df_puntos.set_index('Name')['Points'])

except Exception as e:
    st.error("Asegúrate de que los nombres de los archivos CSV en GitHub sean exactos.")
