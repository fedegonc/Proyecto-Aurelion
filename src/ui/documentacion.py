"""
Componente de vista: Documentación del Proyecto
"""
import streamlit as st
import pandas as pd


def render(loader, analizador):
    """Renderiza la vista de Documentación."""
    st.header("📋 Documentación del Proyecto")
    
    st.subheader("🎯 Tema")
    st.markdown("Inteligencia de negocio para una cadena minorista con presencia en Córdoba.")
    
    st.subheader("❌ Problema")
    st.markdown(
        "El directorio no tiene visibilidad consolidada de dónde, qué y a quién vende más, "
        "dificultando decisiones sobre marketing, inventario y fidelización."
    )
    
    st.subheader("✅ Solución")
    st.markdown(
        "Pipeline analítico con pandas que integra cuatro tablas para generar reportes, "
        "visualizaciones e insights accionables."
    )
    
    st.subheader("📊 Resultado")
    st.markdown(
        "Sistema web interactivo que permite analizar ventas por ciudad, categorías, "
        "clientes VIP, medios de pago y tendencias de precios."
    )
    
    st.divider()
    
    st.subheader("🔄 Flujo del Programa")
    st.markdown(
        "1. **Usuario abre** → `streamlit run app_web.py`\n"
        "2. **Carga datos** → Lee 4 Excel desde `data/raw/`\n"
        "3. **Normaliza** → Limpia columnas y tipifica fechas\n"
        "4. **Integra** → Une las 4 tablas en una maestra\n"
        "5. **Usuario elige** → Selecciona opción del menú\n"
        "6. **Calcula** → Genera métricas de la vista\n"
        "7. **Muestra** → Gráficos, tablas e insights"
    )
    
    st.divider()
    
    st.subheader("📂 Resumen de Datos")
    datos_resumen = pd.DataFrame([
        {"Tabla": "Clientes", "Registros": len(loader.df_clientes), "Descripción": "Datos de clientes con ciudad"},
        {"Tabla": "Productos", "Registros": len(loader.df_productos), "Descripción": "Catálogo con categoría"},
        {"Tabla": "Ventas", "Registros": len(loader.df_ventas), "Descripción": "Transacciones con fecha y medio de pago"},
        {"Tabla": "Detalle", "Registros": len(loader.df_detalle), "Descripción": "Detalle por ítem con cantidad y precio"}
    ])
    st.table(datos_resumen)
    
    st.subheader("🔧 Optimización de Tablas")
    st.markdown(
        "**1. Limpieza:**\n"
        "- Eliminamos `nombre_cliente` y `email` de Ventas (ya están en Clientes)\n"
        "- Eliminamos `nombre_producto` de Detalle (ya está en Productos)\n"
        "- Convertimos `fecha` a tipo `datetime` para análisis temporal\n\n"
        "**2. Integración:**\n"
        "- Unimos Detalle + Ventas por `id_venta`\n"
        "- Agregamos ciudad desde Clientes por `id_cliente`\n"
        "- Agregamos categoría desde Productos por `id_producto`\n"
        "- Resultado: 1 tabla maestra con toda la información\n\n"
        "**3. Beneficio:**\n"
        "- Sin duplicación de datos\n"
        "- Consultas más rápidas\n"
        "- Análisis directo sin joins repetidos"
    )
    
    st.markdown("**Ejemplo de estructura:**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Antes (4 tablas separadas):**")
        ejemplo_antes = pd.DataFrame([
            {"Tabla": "Clientes", "Columnas": "id_cliente, nombre, ciudad"},
            {"Tabla": "Productos", "Columnas": "id_producto, nombre, categoria"},
            {"Tabla": "Ventas", "Columnas": "id_venta, fecha, medio_pago"},
            {"Tabla": "Detalle", "Columnas": "id_venta, id_producto, cantidad"}
        ])
        st.dataframe(ejemplo_antes, width='stretch', hide_index=True)
    
    with col2:
        st.markdown("**Después (1 tabla maestra):**")
        ejemplo_despues = pd.DataFrame([
            {"Columna": "id_venta, id_cliente, id_producto"},
            {"Columna": "fecha, medio_pago, importe"},
            {"Columna": "cantidad, precio_unitario"},
            {"Columna": "ciudad, categoria, nombre_producto"}
        ])
        st.dataframe(ejemplo_despues, width='stretch', hide_index=True)
