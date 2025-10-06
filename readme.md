# Proyecto Aurelion

Sistema de análisis de ventas minoristas con enfoque en inteligencia de negocio.

## 🎯 Objetivo

Transformar datos transaccionales en métricas accionables para decisiones estratégicas de marketing, inventario y expansión geográfica.

## 🚀 Uso Rápido

### Opción 1: Aplicación Web con Streamlit (Recomendado) 🌐

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar aplicación web
streamlit run app_web.py
```

La aplicación web ofrece:
- ✅ Interfaz visual interactiva en HTML
- ✅ Gráficos dinámicos y tablas
- ✅ 6 análisis clave de negocio
- ✅ Se abre automáticamente en el navegador

### Opción 2: Aplicación CLI (Terminal)

```bash
pip install pandas openpyxl
python app.py
```

### Opción 3: Notebooks Jupyter

```bash
pip install -r requirements.txt
jupyter notebook notebooks/normalizacion_y_analisis.ipynb
```

## 📊 Análisis Disponibles

1. **Ventas por Ciudad** → Priorizar mercados
2. **Ranking de Categorías** → Optimizar inventario
3. **Segmentación de Clientes VIP** → Campañas dirigidas
4. **Medios de Pago** → Negociar comisiones
5. **Tendencia de Precios** → Estrategia de pricing
6. **Top Productos** → Gestión de stock

## 📁 Estructura

```
├── data/
│   └── raw/              # Archivos Excel originales
├── src/
│   ├── data_loader.py    # Carga y normalización
│   ├── analizador.py     # Lógica de análisis
│   └── cli.py            # Interfaz CLI
├── notebooks/            # Análisis exploratorios
├── app.py                # Punto de entrada CLI
├── test_app.py           # Suite de pruebas
└── Documentacion.md      # Problema, solución y pseudocódigo

```

## 🧪 Verificar Instalación

```bash
python test_app.py
```

## 📋 Requisitos

- Python 3.8+
- pandas >= 2.0.0
- openpyxl >= 3.1.0
