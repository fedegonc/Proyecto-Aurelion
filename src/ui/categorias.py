"""
Componente de vista: Ranking de Categorías
"""
import streamlit as st
import pandas as pd


def render(loader, analizador):
    """Renderiza la vista de Ranking de Categorías."""
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
