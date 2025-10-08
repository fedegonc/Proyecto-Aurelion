"""
Componente de vista: Tendencia de Precios
"""
import streamlit as st
import pandas as pd


def render(loader, analizador):
    """Renderiza la vista de Tendencia de Precios."""
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
