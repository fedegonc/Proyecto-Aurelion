"""
Aplicación web con Streamlit para análisis de ventas.
Ejecutar: streamlit run app_web.py
"""
import streamlit as st
import pandas as pd
from src.data_loader import DataLoader
from src.analizador import AnalizadorVentas

# Configuración de la página
st.set_page_config(
    page_title="Análisis de Ventas - Proyecto Aurelion",
    page_icon="📊",
    layout="wide"
)

# Título principal
st.title("📊 Sistema de Análisis de Ventas")
st.markdown("### Proyecto Aurelion - Inteligencia de Negocio")
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

st.success(f"✅ Datos cargados: {len(loader.df_clientes)} clientes, {len(loader.df_productos)} productos, {len(loader.df_ventas)} ventas")

# Sidebar para navegación
st.sidebar.title("📋 Menú de Análisis")
opcion = st.sidebar.radio(
    "Selecciona un análisis:",
    [
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
if opcion == "🏠 Resumen General":
    st.header("Resumen General del Negocio")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Clientes", len(loader.df_clientes))
    with col2:
        st.metric("Total Productos", len(loader.df_productos))
    with col3:
        st.metric("Total Ventas", len(loader.df_ventas))
    with col4:
        ventas_ciudad = analizador.ventas_por_ciudad()
        st.metric("Ventas Totales", f"${ventas_ciudad.sum():,.0f}")
    
    st.divider()
    
    # Métricas rápidas
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🏙️ Top 3 Ciudades")
        ventas_ciudad = analizador.ventas_por_ciudad().head(3)
        for ciudad, monto in ventas_ciudad.items():
            st.write(f"**{ciudad}:** ${monto:,.0f}")
    
    with col2:
        st.subheader("📦 Top 3 Categorías")
        ranking = analizador.ranking_categorias()
        for cat, monto in ranking['por_importe'].head(3).items():
            st.write(f"**{cat}:** ${monto:,.0f}")

elif opcion == "🏙️ Ventas por Ciudad":
    st.header("Ventas Totales por Ciudad")
    
    resultado = analizador.ventas_por_ciudad()
    
    # Calcular ticket promedio por ciudad
    df_master = loader.obtener_tabla_maestra()
    ventas_agregadas = df_master.groupby(['ciudad', 'id_venta'])['importe'].sum().reset_index()
    ticket_promedio = ventas_agregadas.groupby('ciudad')['importe'].mean().sort_values(ascending=False)
    
    # Gráficos lado a lado
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Ventas Totales")
        st.bar_chart(resultado)
    
    with col2:
        st.subheader("Ticket Promedio")
        st.bar_chart(ticket_promedio)
    
    # Tabla combinada
    st.subheader("Detalle por Ciudad")
    df_display = pd.DataFrame({
        'Ciudad': resultado.index,
        'Ventas Totales': resultado.values,
        'Ticket Promedio': [ticket_promedio.get(c, 0) for c in resultado.index]
    })
    df_display['Ventas Totales'] = df_display['Ventas Totales'].apply(lambda x: f"${x:,.0f}")
    df_display['Ticket Promedio'] = df_display['Ticket Promedio'].apply(lambda x: f"${x:,.0f}")
    st.dataframe(df_display, width='stretch')
    
    # Insights
    ciudad_top = resultado.index[0]
    monto_top = resultado.iloc[0]
    ciudad_mejor_ticket = ticket_promedio.index[0]
    ticket_top = ticket_promedio.iloc[0]
    
    st.info(f"💡 **Insights:**\n- {ciudad_top} lidera en ventas totales con ${monto_top:,.0f}\n- {ciudad_mejor_ticket} tiene el mejor ticket promedio: ${ticket_top:,.0f}")

elif opcion == "📦 Ranking de Categorías":
    st.header("Análisis de Categorías")
    
    resultado = analizador.ranking_categorias()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Por Importe (Rentabilidad)")
        st.bar_chart(resultado['por_importe'])
        
        df_importe = pd.DataFrame({
            'Categoría': resultado['por_importe'].index,
            'Importe': resultado['por_importe'].values
        })
        df_importe['Importe'] = df_importe['Importe'].apply(lambda x: f"${x:,.0f}")
        st.dataframe(df_importe, width='stretch')
    
    with col2:
        st.subheader("Por Cantidad (Rotación)")
        st.bar_chart(resultado['por_cantidad'])
        
        df_cantidad = pd.DataFrame({
            'Categoría': resultado['por_cantidad'].index,
            'Cantidad': resultado['por_cantidad'].values
        })
        df_cantidad['Cantidad'] = df_cantidad['Cantidad'].apply(lambda x: f"{x:,.0f} unidades")
        st.dataframe(df_cantidad, width='stretch')
    
    # Insights
    cat_top_importe = resultado['por_importe'].index[0]
    cat_top_cantidad = resultado['por_cantidad'].index[0]
    st.info(f"💡 **Insights:**\n- '{cat_top_importe}' genera más ingresos\n- '{cat_top_cantidad}' tiene mayor rotación")

elif opcion == "👥 Segmentación de Clientes VIP":
    st.header("Segmentación de Clientes por Valor (AOV)")
    
    # Leyenda de AOV
    st.info("📖 **AOV (Average Order Value):** Valor promedio de compra por cliente. Se calcula dividiendo el gasto total entre el número de transacciones.")
    
    percentil = st.slider("Percentil para clientes VIP", 50, 99, 90)
    resultado = analizador.segmentacion_clientes(percentil=percentil)
    
    # Agregar información de clientes (nombre y ciudad)
    resultado = resultado.merge(
        loader.df_clientes[['id_cliente', 'nombre_cliente', 'ciudad']],
        on='id_cliente',
        how='left'
    )
    
    # Obtener productos comprados por cada cliente
    df_master = loader.obtener_tabla_maestra()
    productos_por_cliente = df_master.groupby('id_cliente')['nombre_producto'].apply(
        lambda x: ', '.join(x.unique()[:3]) + ('...' if len(x.unique()) > 3 else '')
    ).reset_index()
    productos_por_cliente.columns = ['id_cliente', 'productos_comprados']
    
    resultado = resultado.merge(productos_por_cliente, on='id_cliente', how='left')
    
    # Métricas generales
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Clientes", len(resultado))
    with col2:
        num_vip = resultado['es_vip'].sum()
        st.metric("Clientes VIP", num_vip)
    with col3:
        aov_promedio = resultado['aov'].mean()
        st.metric("AOV Promedio", f"${aov_promedio:,.0f}")
    
    # Top 10 clientes
    st.subheader("Top 10 Clientes por AOV")
    top_10 = resultado.head(10).copy()
    
    # Formatear para mostrar
    top_10_display = pd.DataFrame({
        'ID': top_10['id_cliente'],
        'Nombre': top_10['nombre_cliente'],
        'Ciudad': top_10['ciudad'],
        'Productos Comprados': top_10['productos_comprados'],
        'Total Gasto': top_10['total_gasto'].apply(lambda x: f"${x:,.0f}"),
        'Transacciones': top_10['total_transacciones'].astype(int),
        'AOV (Valor Promedio)': top_10['aov'].apply(lambda x: f"${x:,.0f}")
    })
    
    st.dataframe(top_10_display, width='stretch', hide_index=True)
    
    # Mostrar cuántos son VIP
    num_vip_top10 = top_10['es_vip'].sum()
    st.caption(f"⭐ {num_vip_top10} de estos 10 clientes son VIP (percentil {percentil})")
    
    # Gráficos de análisis
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Distribución de AOV (Top 20)")
        # Usar ID en lugar de nombre para evitar solapamiento
        chart_data = resultado.head(20).copy()
        chart_data['cliente_label'] = 'ID ' + chart_data['id_cliente'].astype(str)
        chart_data = chart_data.set_index('cliente_label')['aov']
        st.bar_chart(chart_data)
    
    with col2:
        st.subheader("Clientes VIP por Ciudad")
        vip_por_ciudad = resultado[resultado['es_vip']].groupby('ciudad').size().sort_values(ascending=False)
        st.bar_chart(vip_por_ciudad)

elif opcion == "💳 Medios de Pago":
    st.header("Análisis de Medios de Pago")
    
    resultado = analizador.medios_de_pago()
    
    # Gráfico de barras
    st.bar_chart(resultado['total_importe'])
    
    # Tabla detallada
    st.subheader("Detalle por Medio de Pago")
    df_display = resultado.copy()
    total_importe = df_display['total_importe'].sum()
    df_display['porcentaje'] = (df_display['total_importe'] / total_importe * 100).apply(lambda x: f"{x:.1f}%")
    df_display['total_importe'] = df_display['total_importe'].apply(lambda x: f"${x:,.0f}")
    df_display['num_transacciones'] = df_display['num_transacciones'].apply(lambda x: f"{x:.0f}")
    
    st.dataframe(df_display, width='stretch')
    
    # Insight
    medio_top = resultado.index[0]
    st.info(f"💡 **Insight:** '{medio_top}' es el medio de pago dominante")

elif opcion == "📈 Tendencia de Precios":
    st.header("Tendencia de Precios Promedio por Categoría")
    
    resultado = analizador.tendencia_precios()
    
    # Selector de categoría
    categorias = resultado['categoria'].unique()
    categoria_seleccionada = st.selectbox("Selecciona una categoría:", categorias)
    
    # Filtrar por categoría
    datos_cat = resultado[resultado['categoria'] == categoria_seleccionada]
    
    # Gráfico de línea
    st.line_chart(datos_cat.set_index('mes')['precio_unitario'])
    
    # Tabla
    st.subheader("Detalle de Precios")
    df_display = datos_cat.copy()
    df_display['precio_unitario'] = df_display['precio_unitario'].apply(lambda x: f"${x:,.2f}")
    st.dataframe(df_display[['mes', 'precio_unitario']], width='stretch')
    
    st.info("💡 **Insight:** Analiza la volatilidad para ajustar estrategias de precios")

elif opcion == "🔝 Top 10 Productos":
    st.header("Top 10 Productos por Cantidad Vendida")
    
    resultado = analizador.top_productos_cantidad(top_n=10)
    
    # Gráfico de barras
    st.bar_chart(resultado)
    
    # Tabla
    st.subheader("Detalle")
    df_display = pd.DataFrame({
        'Producto': resultado.index,
        'Cantidad Vendida': resultado.values
    })
    df_display['Ranking'] = range(1, len(df_display) + 1)
    df_display['Cantidad Vendida'] = df_display['Cantidad Vendida'].apply(lambda x: f"{x:,.0f} unidades")
    
    st.dataframe(
        df_display[['Ranking', 'Producto', 'Cantidad Vendida']],
        width='stretch'
    )
    
    st.info("💡 **Insight:** Prioriza el inventario de estos productos de alta rotación")

# Footer
st.divider()
st.markdown("**Proyecto Aurelion** - Sistema de Análisis de Ventas | Desarrollado con Streamlit")
