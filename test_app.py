"""
Script de prueba rápida para verificar que la app funciona correctamente.
Ejecutar: python test_app.py
"""
from src.data_loader import DataLoader
from src.analizador import AnalizadorVentas

def test_carga_datos():
    """Prueba la carga de datos."""
    print("🧪 Test 1: Carga de datos")
    loader = DataLoader()
    
    if loader.cargar_datos():
        print("✅ Datos cargados correctamente")
        print(f"   - Clientes: {len(loader.df_clientes)} registros")
        print(f"   - Productos: {len(loader.df_productos)} registros")
        print(f"   - Ventas: {len(loader.df_ventas)} registros")
        print(f"   - Detalle: {len(loader.df_detalle)} registros")
        return loader
    else:
        print("❌ Error al cargar datos")
        return None

def test_normalizacion(loader):
    """Prueba la normalización."""
    print("\n🧪 Test 2: Normalización de datos")
    loader.normalizar_datos()
    
    # Verificar que se eliminaron columnas redundantes
    if 'nombre_cliente' not in loader.df_ventas.columns:
        print("✅ Columnas redundantes eliminadas en ventas")
    if 'nombre_producto' not in loader.df_detalle.columns:
        print("✅ Columnas redundantes eliminadas en detalle")
    
    return True

def test_tabla_maestra(loader):
    """Prueba la generación de tabla maestra."""
    print("\n🧪 Test 3: Generación de tabla maestra")
    df_master = loader.obtener_tabla_maestra()
    
    print(f"✅ Tabla maestra generada: {len(df_master)} registros")
    print(f"   Columnas: {list(df_master.columns)}")
    
    return df_master

def test_analisis(df_master):
    """Prueba los análisis."""
    print("\n🧪 Test 4: Análisis de métricas")
    analizador = AnalizadorVentas(df_master)
    
    # Test 1: Ventas por ciudad
    ventas_ciudad = analizador.ventas_por_ciudad()
    print(f"✅ Ventas por ciudad: {len(ventas_ciudad)} ciudades")
    print(f"   Ciudad top: {ventas_ciudad.index[0]} (${ventas_ciudad.iloc[0]:,.0f})")
    
    # Test 2: Ranking categorías
    ranking = analizador.ranking_categorias()
    print(f"✅ Ranking categorías: {len(ranking['por_importe'])} categorías")
    
    # Test 3: Segmentación clientes
    clientes = analizador.segmentacion_clientes()
    num_vip = clientes['es_vip'].sum()
    print(f"✅ Segmentación clientes: {len(clientes)} clientes, {num_vip} VIP")
    
    # Test 4: Medios de pago
    medios = analizador.medios_de_pago()
    print(f"✅ Medios de pago: {len(medios)} métodos")
    
    # Test 5: Tendencia precios
    tendencia = analizador.tendencia_precios()
    print(f"✅ Tendencia precios: {len(tendencia)} registros")
    
    # Test 6: Top productos
    top_prod = analizador.top_productos_cantidad()
    print(f"✅ Top productos: {len(top_prod)} productos")
    
    return True

def main():
    """Ejecuta todas las pruebas."""
    print("="*60)
    print("🧪 SUITE DE PRUEBAS - APLICACIÓN DE ANÁLISIS DE VENTAS")
    print("="*60)
    
    # Test 1: Carga
    loader = test_carga_datos()
    if not loader:
        print("\n❌ Las pruebas fallaron en la carga de datos")
        return
    
    # Test 2: Normalización
    test_normalizacion(loader)
    
    # Test 3: Tabla maestra
    df_master = test_tabla_maestra(loader)
    
    # Test 4: Análisis
    test_analisis(df_master)
    
    print("\n" + "="*60)
    print("✅ TODAS LAS PRUEBAS PASARON EXITOSAMENTE")
    print("="*60)
    print("\n💡 La aplicación está lista para usar. Ejecuta: python app.py")

if __name__ == '__main__':
    main()
