"""
Aplicación web con Streamlit para análisis de ventas.
Ejecutar: streamlit run app_web.py
"""
import streamlit as st
from src.data_loader import DataLoader
from src.analizador import AnalizadorVentas
from src.ui import documentacion, prompts, resumen, ventas_ciudad, categorias, clientes_vip, medios_pago, tendencia_precios, top_productos

# Configuración de la página
st.set_page_config(
    page_title="Análisis de Ventas - Proyecto Aurelion",
    page_icon="📊",
    layout="wide"
)

# CSS para compactar espacios
st.markdown("""
<style>
    .block-container {padding-top: 2rem; padding-bottom: 1rem;}
    h1 {font-size: 2rem; margin-bottom: 0.5rem;}
    h2 {font-size: 1.5rem; margin-top: 1rem; margin-bottom: 0.5rem;}
    h3 {font-size: 1.2rem; margin-top: 0.8rem; margin-bottom: 0.4rem;}
    .stMarkdown {margin-bottom: 0.5rem;}
</style>
""", unsafe_allow_html=True)

# Título principal
st.title("📊 Sistema de Análisis de Ventas")
st.markdown("**Proyecto Aurelion - Inteligencia de Negocio**")
st.divider()

# Cargar datos (con caché para mejor rendimiento)
@st.cache_data
def cargar_y_procesar_datos():
    """Carga y procesa los datos una sola vez."""
    loader = DataLoader()
    if not loader.cargar_datos():
        return None, None
    loader.normalizar_datos()
    df_master = loader.obtener_tabla_maestra()
    analizador = AnalizadorVentas(df_master)
    return loader, analizador

# Cargar datos
with st.spinner('⏳ Cargando datos...'):
    loader, analizador = cargar_y_procesar_datos()

if loader is None:
    st.error("❌ Error al cargar los datos. Verifica que existan en data/raw/")
    st.stop()

st.success(f"✅ {len(loader.df_clientes)} clientes | {len(loader.df_productos)} productos | {len(loader.df_ventas)} ventas")

# Sidebar para navegación
st.sidebar.title("📋 Menú de Análisis")
opcion = st.sidebar.radio(
    "Selecciona un análisis:",
    [
        "📋 Documentación",
        "💬 Prompts Utilizados",
        "🏠 Resumen General",
        "🏙️ Ventas por Ciudad",
        "📦 Ranking de Categorías",
        "👥 Segmentación de Clientes VIP",
        "💳 Medios de Pago",
        "📈 Tendencia de Precios",
        "🔝 Top 10 Productos"
    ]
)

# Contenido principal según opción seleccionada
if opcion == "📋 Documentación":
    documentacion.render(loader, analizador)

elif opcion == "💬 Prompts Utilizados":
    prompts.render(loader, analizador)

elif opcion == "🏠 Resumen General":
    resumen.render(loader, analizador)

elif opcion == "🏙️ Ventas por Ciudad":
    ventas_ciudad.render(loader, analizador)

elif opcion == "📦 Ranking de Categorías":
    categorias.render(loader, analizador)

elif opcion == "👥 Segmentación de Clientes VIP":
    clientes_vip.render(loader, analizador)

elif opcion == "💳 Medios de Pago":
    medios_pago.render(loader, analizador)

elif opcion == "📈 Tendencia de Precios":
    tendencia_precios.render(loader, analizador)

elif opcion == "🔝 Top 10 Productos":
    top_productos.render(loader, analizador)

# Footer
st.divider()
st.markdown("**Proyecto Aurelion** - Sistema de Análisis de Ventas | Desarrollado con Streamlit")
