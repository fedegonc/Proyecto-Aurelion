# 📱 Aplicación CLI de Análisis de Ventas

## 🚀 Instalación y Ejecución

### 1. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 2. Ejecutar la aplicación
```bash
python app.py
```

## 📊 Funcionalidades

La aplicación ofrece **6 análisis principales** basados en métricas clave de negocio:

### 1️⃣ Ventas por Ciudad
- **Métrica:** Ventas totales por ubicación geográfica
- **Insight:** Identifica mercados prioritarios

### 2️⃣ Ranking de Categorías
- **Métricas:** 
  - Por importe (rentabilidad)
  - Por cantidad (rotación)
- **Insight:** Optimiza mix de productos

### 3️⃣ Segmentación de Clientes VIP
- **Métrica:** AOV (Average Order Value) por cliente
- **Insight:** Identifica clientes de alto valor (percentil 90)

### 4️⃣ Análisis de Medios de Pago
- **Métrica:** Distribución de transacciones por método
- **Insight:** Optimiza costos de comisiones bancarias

### 5️⃣ Tendencia de Precios
- **Métrica:** Evolución de precios promedio por categoría/mes
- **Insight:** Detecta volatilidad y oportunidades de pricing

### 6️⃣ Top 10 Productos por Cantidad
- **Métrica:** Productos de mayor rotación
- **Insight:** Prioriza inventario

### 7️⃣ Reporte Completo
- Ejecuta todos los análisis secuencialmente

## 🎯 Principios de Diseño

- **KISS (Keep It Simple):** Interfaz minimalista sin gráficos HTML
- **DRY (Don't Repeat Yourself):** Código modular y reutilizable
- **Coherencia:** Flujo lógico de métricas de negocio

## 📁 Estructura del Código

```
src/
├── data_loader.py   # Carga y normalización de datos
├── analizador.py    # Lógica de análisis (5 métricas principales)
└── cli.py           # Interfaz de usuario en terminal

app.py               # Punto de entrada
```

## 💡 Uso Típico

1. Ejecuta `python app.py`
2. Los datos se cargan automáticamente desde `data/raw/`
3. Selecciona el análisis que necesitas (1-7)
4. Visualiza resultados en formato tabla ASCII
5. Presiona ENTER para volver al menú

## ⚠️ Requisitos

- Python 3.8+
- pandas >= 2.0.0
- openpyxl >= 3.1.0
- Archivos Excel en `data/raw/`:
  - clientes.xlsx
  - productos.xlsx
  - ventas.xlsx
  - detalle_ventas.xlsx
