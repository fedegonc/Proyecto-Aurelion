"""
Componente de vista: Resumen General
"""
import streamlit as st


def render(loader, analizador):
    """Renderiza la vista de Resumen General."""
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
        top_ciudades = ventas_ciudad.head(3)
        for ciudad, monto in top_ciudades.items():
            st.write(f"**{ciudad}:** ${monto:,.0f}")
    
    with col2:
        st.subheader("📦 Top 3 Categorías")
        ranking = analizador.ranking_categorias()
        for cat, monto in ranking['por_importe'].head(3).items():
            st.write(f"**{cat}:** ${monto:,.0f}")
