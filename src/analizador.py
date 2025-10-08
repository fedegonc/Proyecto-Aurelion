"""
Módulo de análisis de métricas clave de negocio.
Implementa los 5 análisis principales identificados en la documentación.
"""
import pandas as pd


class AnalizadorVentas:
    """Realiza análisis descriptivos sobre los datos de ventas."""
    
    def __init__(self, df_master):
        self.df = df_master
    
    def _calcular_ventas_totales(self):
        """Calcula importe total por venta (método auxiliar)."""
        ventas = self.df.groupby('id_venta')['importe'].sum().reset_index()
        ventas.rename(columns={'importe': 'importe_total_venta'}, inplace=True)
        return ventas
        
    def ventas_por_ciudad(self):
        """
        Análisis 1: Ventas totales por ciudad.
        Métrica clave: ¿Dónde vendemos más?
        """
        resultado = self.df.groupby('ciudad')['importe'].sum().sort_values(ascending=False)
        return resultado
    
    def ranking_categorias(self):
        """
        Análisis 2: Ranking de categorías por importe y cantidad.
        Métrica clave: ¿Qué productos generan más ingresos y rotación?
        """
        por_importe = self.df.groupby('categoria')['importe'].sum().sort_values(ascending=False)
        por_cantidad = self.df.groupby('categoria')['cantidad'].sum().sort_values(ascending=False)
        
        return {
            'por_importe': por_importe,
            'por_cantidad': por_cantidad
        }
    
    def segmentacion_clientes(self, percentil=90):
        """
        Análisis 3: Segmentación de clientes por valor promedio (AOV).
        Métrica clave: ¿Quiénes son nuestros clientes VIP?
        """
        ventas_totales = self._calcular_ventas_totales()
        
        # Unir con información de cliente
        df_aov = ventas_totales.merge(
            self.df[['id_venta', 'id_cliente']].drop_duplicates(),
            on='id_venta'
        )
        
        # Calcular métricas por cliente
        metricas = df_aov.groupby('id_cliente').agg(
            total_gasto=('importe_total_venta', 'sum'),
            total_transacciones=('id_venta', 'nunique')
        ).reset_index()
        
        metricas['aov'] = metricas['total_gasto'] / metricas['total_transacciones']
        
        # Identificar clientes VIP (percentil especificado)
        umbral_vip = metricas['aov'].quantile(percentil / 100)
        metricas['es_vip'] = metricas['aov'] >= umbral_vip
        
        return metricas.sort_values('aov', ascending=False)
    
    def medios_de_pago(self):
        """
        Análisis 4: Distribución de transacciones por medio de pago.
        Métrica clave: ¿Cómo prefieren pagar nuestros clientes?
        """
        ventas_totales = self._calcular_ventas_totales()
        
        # Unir con medio de pago
        df_pagos = ventas_totales.merge(
            self.df[['id_venta', 'medio_pago']].drop_duplicates(),
            on='id_venta'
        )
        
        # Agrupar por medio de pago
        resultado = df_pagos.groupby('medio_pago').agg(
            total_importe=('importe_total_venta', 'sum'),
            num_transacciones=('id_venta', 'count')
        ).sort_values('total_importe', ascending=False)
        
        return resultado
    
    def tendencia_precios(self):
        """
        Análisis 5: Evolución de precios promedio por categoría y mes.
        Métrica clave: ¿Cómo varían los precios en el tiempo?
        """
        # Extraer mes de la fecha
        df_temp = self.df.copy()
        df_temp['mes'] = df_temp['fecha'].dt.to_period('M')
        
        # Calcular precio promedio por categoría y mes
        resultado = df_temp.groupby(['mes', 'categoria'])['precio_unitario'].mean().reset_index()
        resultado['mes'] = resultado['mes'].astype(str)
        
        return resultado
    
    def top_productos_cantidad(self, top_n=10):
        """
        Análisis adicional: Top N productos por cantidad vendida.
        Métrica clave: ¿Qué productos tienen mayor rotación?
        """
        resultado = self.df.groupby('nombre_producto')['cantidad'].sum().sort_values(ascending=False).head(top_n)
        return resultado
