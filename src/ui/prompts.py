"""
Componente de vista: Prompts Utilizados
"""
import streamlit as st
import pandas as pd


def render(loader, analizador):
    """Renderiza la vista de Prompts del Proyecto."""
    st.header("💬 Prompts Utilizados en el Proyecto")
    
    st.markdown(
        "Esta sección documenta los prompts que guiaron el desarrollo del proyecto, "
        "mostrando ejemplos aceptados (que generaron valor) y rechazados (que no aportaron)."
    )
    
    st.divider()
    
    # Tabla de prompts
    prompts_data = pd.DataFrame([
        {
            "Tipo": "✅ Aceptado",
            "Prompt": "Analiza ventas por ciudad para priorizar mercados",
            "Razón": "Identifica dónde concentrar esfuerzos de marketing"
        },
        {
            "Tipo": "❌ Rechazado",
            "Prompt": "Crea dashboard con 20 métricas diferentes",
            "Razón": "Sobrecarga de información, dificulta decisiones"
        },
        {
            "Tipo": "✅ Aceptado",
            "Prompt": "Segmenta clientes VIP para campañas dirigidas",
            "Razón": "Identifica clientes de alto valor para fidelización"
        },
        {
            "Tipo": "❌ Rechazado",
            "Prompt": "Agrega campo para cargar Excel desde la interfaz",
            "Razón": "Ahora hardcodeado en data/raw/, pero sería mejor para el futuro"
        },
        {
            "Tipo": "✅ Aceptado",
            "Prompt": "Identifica productos de alta rotación",
            "Razón": "Optimiza inventario y evita desabastecimientos"
        },
        {
            "Tipo": "❌ Rechazado",
            "Prompt": "Crea sistema de recomendaciones personalizado",
            "Razón": "Fuera del alcance, requiere datos históricos de comportamiento"
        },
        {
            "Tipo": "✅ Aceptado",
            "Prompt": "Analiza medios de pago para negociar comisiones",
            "Razón": "Reduce costos operativos bancarios"
        },
        {
            "Tipo": "❌ Rechazado",
            "Prompt": "Integra con redes sociales",
            "Razón": "No aporta al análisis de ventas actual"
        }
    ])
    
    st.subheader("📊 Tabla de Prompts")
    
    # Filtro
    filtro = st.radio("Filtrar por:", ["Todos", "✅ Aceptados", "❌ Rechazados"], horizontal=True)
    
    if filtro == "✅ Aceptados":
        prompts_filtrados = prompts_data[prompts_data["Tipo"] == "✅ Aceptado"]
    elif filtro == "❌ Rechazados":
        prompts_filtrados = prompts_data[prompts_data["Tipo"] == "❌ Rechazado"]
    else:
        prompts_filtrados = prompts_data
    
    st.dataframe(prompts_filtrados, width='stretch', hide_index=True)
    
    st.divider()
    
    st.subheader("📝 Lecciones Aprendidas")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**✅ Prompts Efectivos:**")
        st.markdown(
            "- Específicos y accionables\n"
            "- Generan insights de negocio\n"
            "- Simplifican decisiones\n"
            "- Siguen principios KISS y DRY"
        )
    
    with col2:
        st.markdown("**❌ Prompts Inefectivos:**")
        st.markdown(
            "- Demasiado genéricos o complejos\n"
            "- Sobreingeniería prematura\n"
            "- Fuera del alcance del proyecto\n"
            "- No aportan valor inmediato"
        )
