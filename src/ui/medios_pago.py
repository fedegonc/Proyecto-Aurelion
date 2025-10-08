"""
Componente de vista: Medios de Pago
"""
import streamlit as st
import pandas as pd


def render(loader, analizador):
    """Renderiza la vista de Medios de Pago."""
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
