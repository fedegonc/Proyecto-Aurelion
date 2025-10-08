"""
Componente de vista: Top 10 Productos
"""
import streamlit as st
import pandas as pd


def render(loader, analizador):
    """Renderiza la vista de Top 10 Productos."""
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
