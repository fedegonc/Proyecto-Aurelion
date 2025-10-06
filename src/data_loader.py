"""
Módulo de carga y normalización de datos.
Principios: KISS (Keep It Simple) y DRY (Don't Repeat Yourself)
"""
import pandas as pd
import os


class DataLoader:
    """Carga y normaliza los datos de ventas desde archivos Excel."""
    
    def __init__(self, raw_path='data/raw/'):
        self.raw_path = raw_path
        self.df_clientes = None
        self.df_productos = None
        self.df_ventas = None
        self.df_detalle = None
        
    def cargar_datos(self):
        """Carga los 4 archivos Excel desde data/raw/"""
        try:
            self.df_clientes = pd.read_excel(os.path.join(self.raw_path, 'clientes.xlsx'))
            self.df_productos = pd.read_excel(os.path.join(self.raw_path, 'productos.xlsx'))
            self.df_ventas = pd.read_excel(os.path.join(self.raw_path, 'ventas.xlsx'))
            self.df_detalle = pd.read_excel(os.path.join(self.raw_path, 'detalle_ventas.xlsx'))
            return True
        except FileNotFoundError as e:
            print(f"❌ Error: No se encontró el archivo {e.filename}")
            return False
        except Exception as e:
            print(f"❌ Error al cargar datos: {e}")
            return False
    
    def normalizar_datos(self):
        """Elimina columnas redundantes y normaliza las tablas."""
        # Eliminar columnas redundantes en ventas
        self.df_ventas = self.df_ventas.drop(columns=['nombre_cliente', 'email'], errors='ignore')
        
        # Eliminar columnas redundantes en detalle
        self.df_detalle = self.df_detalle.drop(columns=['nombre_producto'], errors='ignore')
        
        # Convertir fecha a datetime
        self.df_ventas['fecha'] = pd.to_datetime(self.df_ventas['fecha'])
        
    def obtener_tabla_maestra(self):
        """
        Integra las 4 tablas en una tabla maestra para análisis.
        Retorna DataFrame con toda la información consolidada.
        """
        # 1. Merge ventas con detalle
        df_master = self.df_detalle.merge(
            self.df_ventas,
            on='id_venta',
            how='left'
        )
        
        # 2. Agregar información de clientes (ciudad)
        df_master = df_master.merge(
            self.df_clientes[['id_cliente', 'ciudad']],
            on='id_cliente',
            how='left'
        )
        
        # 3. Agregar información de productos (categoría)
        df_master = df_master.merge(
            self.df_productos[['id_producto', 'nombre_producto', 'categoria']],
            on='id_producto',
            how='left'
        )
        
        return df_master
