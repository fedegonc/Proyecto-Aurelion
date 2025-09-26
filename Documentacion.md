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
