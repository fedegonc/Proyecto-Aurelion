# Documentación del Proyecto Aurelion

## Tema

- **Análisis de ventas minoristas** para comprender el desempeño comercial de una tienda a partir de los datos disponibles.

## Problema

- **Necesidad**: El equipo directivo no cuenta con una visión integrada de dónde se concentran las ventas (ciudades, categorías y medios de pago) ni del valor promedio que aportan los clientes.
- **Impacto**: Dificultad para priorizar acciones comerciales, optimizar inventario y definir campañas enfocadas.

## Solución

- **Flujo simple** que:
  1. Toma los Excel de `data/raw/` y los deja prolijos en `data/processed/`.
  2. Usa el cuaderno `notebooks/normalizacion_y_analisis.ipynb` para calcular métricas básicas (ventas por ciudad, categoría, medio de pago y ticket promedio).
  3. Muestra tablas y gráficos claros para compartir conclusiones rápidas.

## Estructura de la base de datos

| Tabla               | Campos principales                                               | Descripción                                |
|---------------------|------------------------------------------------------------------|--------------------------------------------|
| `clientes`          | `id_cliente`, `nombre_cliente`, `ciudad`                         | Quién compra y dónde vive                  |
| `productos`         | `id_producto`, `nombre_producto`, `categoria`                    | Qué vendemos                               |
| `ventas`            | `id_venta`, `fecha`, `id_cliente`, `medio_pago`                  | Cada transacción realizada                 |
| `detalle_ventas`    | `id_venta`, `id_producto`, `cantidad`, `precio_unitario`, `importe` | Qué productos incluye cada venta       |

- **Tipos de datos**: números, fechas y texto.
- **Escala actual**: 4 Excel con unas decenas de registros cada uno.

## Información clave disponible

- **Clientes**: Quiénes son y de qué ciudad.
- **Productos**: Categorías disponibles.
- **Ventas**: Cuándo y cómo se cobró.
- **Detalle**: Cantidades e importes por producto.

## Pasos principales

1. Abrimos los Excel crudos y quitamos columnas que no aportan.
2. Guardamos las versiones limpias con sufijo `_proc`.
3. Cruzamos la información para saber dónde se vende más, qué categorías lideran y qué medio de pago domina.
4. Calculamos el ticket promedio por cliente y generamos gráficos para presentar.

## Próximos pasos sugeridos

- **Documentar insights** detectados (ej. ciudad líder, categoría dominante, medio de pago más usado).
- **Explorar sesgos** agregando métricas como participación porcentual por ciudad o serie temporal por mes.
- **Refactorizar** la lógica del notebook en funciones del directorio `src/` para reutilización futura.


# 📈 CONSOLIDACIÓN DE HALLAZGOS Y RECOMENDACIONES

**Objetivo:** Proporcionar un análisis de la estructura de ventas para la toma de decisiones estratégicas de inventario, marketing y precios.

## 1. Estructura de Ventas y Rendimiento Geográfico
* **Ventas Totales por Ciudad:** **Río Cuarto** es el mercado principal (aprox. $792k), seguido de cerca por Alta Gracia y Córdoba capital.
* **Recomendación:** Enfocar las campañas de marketing o las promociones de fidelidad en **Río Cuarto** para maximizar el retorno, y estudiar a **Mendiolaza** (la ciudad más pequeña en ventas) para determinar si es viable expandir la logística allí.

## 2. Desempeño de Productos y Categorías
* **Contribución Financiera (Importe):** La categoría de **Alimentos** es el motor financiero del negocio, representando la mayor parte de los ingresos.
* **Demanda Operacional (Cantidad):** Los productos de bajo costo, como ciertos artículos de Limpieza o Bebidas, dominan el *Top 10* en unidades vendidas.
* **Recomendación:** Optimizar el **inventario** de los productos del Top 10 por cantidad para evitar roturas de stock, y concentrar los esfuerzos de margen en la categoría de **Alimentos**.

## 3. Comportamiento del Cliente y Medios de Pago
* **Valor Promedio de Transacción (AOV):** La mayoría de los clientes tiene un AOV en el rango medio, pero hay un pequeño grupo de clientes *Premium* con un AOV muy alto.
* **Medios de Pago:** El pago con **Tarjeta** o **Efectivo** suele ser el dominante (dependerá de tu gráfico).
* **Recomendación:** Crear programas de incentivo o descuentos dirigidos al *Top 10* de clientes por AOV para fidelizarlos y mantener su alto gasto.

## 4. Conclusión Clave: Tendencia de Precios (Tu Último Gráfico)

Este es el hallazgo más sofisticado y requiere interpretar el gráfico que acabas de generar (Imagen `image_e75586.png`):

* **Tendencia de Precios:** La categoría **Limpieza** muestra una **volatilidad significativa** (grandes picos y valles), lo que sugiere cambios de precios frecuentes o fuertes promociones. Por otro lado, la categoría **Alimentos** es **relativamente más estable**, aunque con una ligera tendencia al alza a partir del mes 04.
* **Recomendación:** Estudiar los picos de precios en la categoría **Limpieza** para entender si corresponden a estrategias promocionales exitosas o a fluctuaciones de costos. Mantener la estabilidad de precios en **Alimentos** para no ahuyentar al mercado principal.