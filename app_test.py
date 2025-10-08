"""
Test simple para verificar que la app funciona.
Ejecutar: python app_test.py
"""
from src.data_loader import DataLoader
from src.analizador import AnalizadorVentas


def run_tests():
    print("\n🧪 Verificando aplicación...\n")
    
    # Test carga y procesamiento
    loader = DataLoader()
    if not loader.cargar_datos():
        print("❌ Error cargando datos")
        return False
    
    loader.normalizar_datos()
    df_master = loader.obtener_tabla_maestra()
    
    if df_master is None or len(df_master) == 0:
        print("❌ Error en tabla maestra")
        return False
    
    # Test analizador
    analizador = AnalizadorVentas(df_master)
    
    tests = [
        analizador.ventas_por_ciudad(),
        analizador.ranking_categorias(),
        analizador.segmentacion_clientes(),
        analizador.medios_de_pago(),
        analizador.tendencia_precios(),
        analizador.top_productos_cantidad()
    ]
    
    if any(t is None or (hasattr(t, '__len__') and len(t) == 0) for t in tests):
        print("❌ Error en funciones de análisis")
        return False
    
    print(f"✅ Todo funciona correctamente")
    print(f"   {len(loader.df_clientes)} clientes | {len(loader.df_ventas)} ventas")
    print(f"\nEjecutar: streamlit run app_web.py\n")
    return True


if __name__ == "__main__":
    run_tests()
