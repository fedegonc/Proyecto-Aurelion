# Proyecto Aurelion

Sistema de análisis de ventas minoristas con enfoque en inteligencia de negocio.

## 🎯 Objetivo

Transformar datos transaccionales en métricas accionables para decisiones estratégicas de marketing, inventario y expansión geográfica.

## 🚀 Instalación y Uso

```bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Ejecutar aplicación web
streamlit run app_web.py
```

**La aplicación se abrirá automáticamente en tu navegador** en `http://localhost:8501`

### ✨ Características:
- ✅ Interfaz visual interactiva
- ✅ 6 análisis clave de negocio
- ✅ Gráficos dinámicos y tablas
- ✅ Navegación intuitiva por sidebar
- ✅ Insights automáticos

## 📊 Análisis Disponibles

1. **Ventas por Ciudad** → Priorizar mercados
2. **Ranking de Categorías** → Optimizar inventario
3. **Segmentación de Clientes VIP** → Campañas dirigidas
4. **Medios de Pago** → Negociar comisiones
5. **Tendencia de Precios** → Estrategia de pricing
6. **Top Productos** → Gestión de stock

## 📁 Estructura del Proyecto

```
Proyecto-Aurelion/
├── data/
│   └── raw/              # Archivos Excel originales
├── src/
│   ├── data_loader.py    # Carga y normalización de datos
│   └── analizador.py     # Lógica de análisis de negocio
├── notebooks/            # Análisis exploratorios (Jupyter)
├── app_web.py            # Aplicación web principal
├── Documentacion.md      # Problema, solución y pseudocódigo
└── requirements.txt      # Dependencias del proyecto
```

## 📋 Requisitos

- Python 3.8+
- pandas >= 2.0.0
- openpyxl >= 3.1.0
- streamlit >= 1.28.0

## 📖 Documentación Adicional

- **`Documentacion.md`** - Análisis del problema, solución propuesta y pseudocódigo
- **`notebooks/`** - Notebooks Jupyter con análisis exploratorios detallados
