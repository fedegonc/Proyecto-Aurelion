# Proyecto Aurelion

Breve descripción del flujo 80/20 para entender rápido el propósito del repositorio.

## Objetivo

- **Qué hacemos** Procesamos los Excel de `data/raw/` para generar tablas limpias en `data/processed/` y ejecutamos el cuaderno `notebooks/normalizacion_y_analisis.ipynb` para obtener métricas de negocio.
- **Por qué sirve** Entrega una visión inmediata de ventas por ciudad, categoría, medio de pago y ticket promedio (AOV).

## Datos

- **Entrada** `clientes.xlsx`, `productos.xlsx`, `ventas.xlsx`, `detalle_ventas.xlsx` en `data/raw/`.
- **Salida** Versiones normalizadas con sufijo `_proc.xlsx` en `data/processed/`.

## Uso rápido

```bash
pip install -r requirements.txt
jupyter notebook notebooks/normalizacion_y_analisis.ipynb
```

- **Pasos** Ejecuta las celdas en orden; se crearán los archivos procesados y gráficos clave.
- **Requisitos** Tener Python 3.13+ y los paquetes listados (ej. `pandas`, `openpyxl`, `matplotlib`).

## Próximos pasos sugeridos

- **Mejorar storytelling** Agregar celdas Markdown con conclusiones de cada análisis.
- **Automatizar** Migrar la lógica del notebook a funciones en `src/` para reutilizarla desde scripts o pipelines.
