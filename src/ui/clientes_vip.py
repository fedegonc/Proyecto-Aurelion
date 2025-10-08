"""
Componente de vista: Segmentación de Clientes VIP
"""
import streamlit as st
import pandas as pd


def render(loader, analizador):
    """Renderiza la vista de Segmentación de Clientes VIP."""
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
    
    # Obtener productos comprados por cada cliente (usando df ya cargado)
    productos_por_cliente = analizador.df.groupby('id_cliente')['nombre_producto'].apply(
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
