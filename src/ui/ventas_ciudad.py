"""
Componente de vista: Ventas por Ciudad
"""
import streamlit as st
import pandas as pd


def render(loader, analizador):
    """Renderiza la vista de Ventas por Ciudad."""
    st.header("Ventas Totales por Ciudad")
    
    resultado = analizador.ventas_por_ciudad()
    
    # Calcular ticket promedio por ciudad (usando df ya cargado)
    ventas_agregadas = analizador.df.groupby(['ciudad', 'id_venta'])['importe'].sum().reset_index()
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
