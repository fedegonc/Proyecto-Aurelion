# Documentación del Proyecto Aurelion

## 🎯 Problema (Visión de Negocio)

Cadena minorista sin visibilidad consolidada de desempeño comercial. El equipo directivo no identifica dónde concentrar esfuerzos de marketing, qué productos optimizar en inventario, ni qué clientes fidelizar. Impacto: campañas genéricas, desabastecimientos y pérdida de oportunidades de crecimiento geográfico.

**Pregunta clave:** ¿Dónde, qué y a quién vendemos más para maximizar rentabilidad?

## ✅ Solución

Pipeline de análisis descriptivo con **pandas** que integra 4 tablas (clientes, productos, ventas, detalle_ventas) para generar:

1. **Ventas por ciudad** → Priorizar mercados
2. **Ranking de categorías** → Optimizar inventario por rentabilidad/rotación
3. **Segmentación de clientes VIP** → Campañas dirigidas (percentil 90 AOV)
4. **Análisis de medios de pago** → Negociar comisiones bancarias
5. **Tendencias temporales** → Estrategia de precios por categoría

**Entregables:** Tablas normalizadas, gráficos (matplotlib/seaborn) y recomendaciones accionables.

## 💻 Pseudocódigo

```
# 1. NORMALIZACIÓN
CARGAR 4 Excel desde data/raw/
ELIMINAR columnas redundantes
CONVERTIR fechas a datetime, IDs a int
GUARDAR en data/processed/ con sufijo _proc

# 2. INTEGRACIÓN
tabla_maestra = MERGE(ventas, detalle_ventas, clientes, productos)

# 3. ANÁLISIS
ventas_ciudad = AGRUPAR POR ciudad → SUM(importe), AVG(ticket)
ventas_categoria = AGRUPAR POR categoria → SUM(importe), SUM(cantidad)
aov_cliente = AGRUPAR POR id_cliente → AVG(importe)
clientes_vip = FILTRAR percentil >= 90
medios_pago = AGRUPAR POR medio_pago → COUNT(*)
tendencia_precios = AGRUPAR POR mes, categoria → AVG(precio_unitario)

# 4. VISUALIZACIÓN
GENERAR gráficos de barras, líneas, histogramas
DOCUMENTAR top 3 hallazgos por análisis
```

**Datos:** 100 clientes, 100 productos, 120 transacciones, 343 líneas de detalle en 4 ciudades de Córdoba.