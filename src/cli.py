"""
CLI principal para análisis de ventas.
Interfaz de usuario simple y clara en terminal (sin HTML).
Principios: KISS y DRY
"""
import sys
import os

# Agregar el directorio raíz al path para imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.data_loader import DataLoader
from src.analizador import AnalizadorVentas


class VentasCLI:
    """Interfaz de línea de comandos para análisis de ventas."""
    
    def __init__(self):
        self.loader = None
        self.analizador = None
        self.datos_cargados = False
        
    def mostrar_banner(self):
        """Muestra el banner de bienvenida."""
        print("\n" + "="*60)
        print(" 📊 SISTEMA DE ANÁLISIS DE VENTAS - PROYECTO AURELION")
        print("="*60)
        
    def mostrar_menu(self):
        """Muestra el menú principal."""
        print("\n┌─ MENÚ PRINCIPAL " + "─"*42 + "┐")
        print("│")
        print("│  1. 🏙️  Ventas por Ciudad")
        print("│  2. 📦 Ranking de Categorías")
        print("│  3. 👥 Segmentación de Clientes (VIP)")
        print("│  4. 💳 Análisis de Medios de Pago")
        print("│  5. 📈 Tendencia de Precios")
        print("│  6. 🔝 Top 10 Productos por Cantidad")
        print("│  7. 📋 Reporte Completo")
        print("│  0. ❌ Salir")
        print("│")
        print("└" + "─"*58 + "┘")
        
    def cargar_datos(self):
        """Carga y normaliza los datos."""
        print("\n⏳ Cargando datos...")
        self.loader = DataLoader()
        
        if not self.loader.cargar_datos():
            return False
            
        print("✅ Datos cargados exitosamente")
        
        print("⏳ Normalizando datos...")
        self.loader.normalizar_datos()
        print("✅ Datos normalizados")
        
        print("⏳ Generando tabla maestra...")
        df_master = self.loader.obtener_tabla_maestra()
        self.analizador = AnalizadorVentas(df_master)
        print("✅ Tabla maestra generada")
        
        self.datos_cargados = True
        return True
    
    def mostrar_tabla(self, datos, titulo, formato_valor='${:,.0f}'):
        """Muestra datos en formato tabla simple."""
        print(f"\n{'─'*60}")
        print(f"📊 {titulo}")
        print('─'*60)
        
        if isinstance(datos, dict):
            for key, value in datos.items():
                print(f"  {key:30} {formato_valor.format(value)}")
        else:
            for idx, valor in datos.items():
                if formato_valor:
                    print(f"  {str(idx):30} {formato_valor.format(valor)}")
                else:
                    print(f"  {str(idx):30} {valor}")
        
        print('─'*60)
    
    def opcion_ventas_ciudad(self):
        """Opción 1: Ventas por ciudad."""
        resultado = self.analizador.ventas_por_ciudad()
        self.mostrar_tabla(resultado, "VENTAS TOTALES POR CIUDAD")
        
        # Insight clave
        ciudad_top = resultado.index[0]
        monto_top = resultado.iloc[0]
        print(f"\n💡 Insight: {ciudad_top} lidera con ${monto_top:,.0f} en ventas")
    
    def opcion_ranking_categorias(self):
        """Opción 2: Ranking de categorías."""
        resultado = self.analizador.ranking_categorias()
        
        print("\n" + "="*60)
        print("📦 ANÁLISIS DE CATEGORÍAS")
        print("="*60)
        
        print("\n🔸 Por Importe (Rentabilidad):")
        for cat, valor in resultado['por_importe'].items():
            print(f"  {cat:20} ${valor:>12,.0f}")
        
        print("\n🔸 Por Cantidad (Rotación):")
        for cat, valor in resultado['por_cantidad'].items():
            print(f"  {cat:20} {valor:>12,.0f} unidades")
        
        print('─'*60)
        
        # Insight clave
        cat_top_importe = resultado['por_importe'].index[0]
        cat_top_cantidad = resultado['por_cantidad'].index[0]
        print(f"\n💡 Insight: '{cat_top_importe}' genera más ingresos")
        print(f"💡 Insight: '{cat_top_cantidad}' tiene mayor rotación")
    
    def opcion_segmentacion_clientes(self):
        """Opción 3: Segmentación de clientes."""
        resultado = self.analizador.segmentacion_clientes(percentil=90)
        
        print("\n" + "="*60)
        print("👥 SEGMENTACIÓN DE CLIENTES (Top 10 por AOV)")
        print("="*60)
        print(f"{'ID':>5} {'Total Gasto':>15} {'Transacciones':>15} {'AOV':>15} {'VIP':>5}")
        print('─'*60)
        
        for _, row in resultado.head(10).iterrows():
            vip_mark = "⭐" if row['es_vip'] else ""
            print(f"{row['id_cliente']:>5} ${row['total_gasto']:>14,.0f} "
                  f"{row['total_transacciones']:>15.0f} ${row['aov']:>14,.0f} {vip_mark:>5}")
        
        print('─'*60)
        
        # Insights
        num_vip = resultado['es_vip'].sum()
        aov_promedio = resultado['aov'].mean()
        print(f"\n💡 Insight: {num_vip} clientes VIP identificados (percentil 90)")
        print(f"💡 AOV promedio general: ${aov_promedio:,.0f}")
    
    def opcion_medios_pago(self):
        """Opción 4: Medios de pago."""
        resultado = self.analizador.medios_de_pago()
        
        print("\n" + "="*60)
        print("💳 ANÁLISIS DE MEDIOS DE PAGO")
        print("="*60)
        print(f"{'Medio de Pago':20} {'Importe Total':>18} {'Transacciones':>15}")
        print('─'*60)
        
        total_importe = resultado['total_importe'].sum()
        
        for medio, row in resultado.iterrows():
            porcentaje = (row['total_importe'] / total_importe) * 100
            print(f"{medio:20} ${row['total_importe']:>17,.0f} "
                  f"{row['num_transacciones']:>15.0f} ({porcentaje:>5.1f}%)")
        
        print('─'*60)
        
        # Insight
        medio_top = resultado.index[0]
        print(f"\n💡 Insight: '{medio_top}' es el medio de pago dominante")
    
    def opcion_tendencia_precios(self):
        """Opción 5: Tendencia de precios."""
        resultado = self.analizador.tendencia_precios()
        
        print("\n" + "="*60)
        print("📈 TENDENCIA DE PRECIOS PROMEDIO POR CATEGORÍA")
        print("="*60)
        
        # Agrupar por categoría
        categorias = resultado['categoria'].unique()
        
        for cat in categorias:
            datos_cat = resultado[resultado['categoria'] == cat]
            print(f"\n🔸 {cat}:")
            for _, row in datos_cat.iterrows():
                print(f"  {row['mes']:10} ${row['precio_unitario']:>10,.2f}")
        
        print('─'*60)
        print("\n💡 Insight: Analiza volatilidad para estrategias de precios")
    
    def opcion_top_productos(self):
        """Opción 6: Top productos por cantidad."""
        resultado = self.analizador.top_productos_cantidad(top_n=10)
        
        print("\n" + "="*60)
        print("🔝 TOP 10 PRODUCTOS POR CANTIDAD VENDIDA")
        print("="*60)
        
        for idx, (producto, cantidad) in enumerate(resultado.items(), 1):
            print(f"  {idx:2}. {producto:40} {cantidad:>8,.0f} unidades")
        
        print('─'*60)
        print("\n💡 Insight: Prioriza inventario de estos productos de alta rotación")
    
    def opcion_reporte_completo(self):
        """Opción 7: Reporte completo."""
        print("\n" + "="*60)
        print("📋 GENERANDO REPORTE COMPLETO")
        print("="*60)
        
        self.opcion_ventas_ciudad()
        input("\n[Presiona ENTER para continuar...]")
        
        self.opcion_ranking_categorias()
        input("\n[Presiona ENTER para continuar...]")
        
        self.opcion_segmentacion_clientes()
        input("\n[Presiona ENTER para continuar...]")
        
        self.opcion_medios_pago()
        input("\n[Presiona ENTER para continuar...]")
        
        self.opcion_top_productos()
        
        print("\n✅ Reporte completo generado")
    
    def ejecutar(self):
        """Ejecuta la aplicación CLI."""
        self.mostrar_banner()
        
        # Cargar datos al inicio
        if not self.cargar_datos():
            print("\n❌ No se pudieron cargar los datos. Verifica que existan en data/raw/")
            return
        
        # Loop principal
        while True:
            self.mostrar_menu()
            
            try:
                opcion = input("\n👉 Selecciona una opción: ").strip()
                
                if opcion == '0':
                    print("\n👋 ¡Hasta luego!")
                    break
                elif opcion == '1':
                    self.opcion_ventas_ciudad()
                elif opcion == '2':
                    self.opcion_ranking_categorias()
                elif opcion == '3':
                    self.opcion_segmentacion_clientes()
                elif opcion == '4':
                    self.opcion_medios_pago()
                elif opcion == '5':
                    self.opcion_tendencia_precios()
                elif opcion == '6':
                    self.opcion_top_productos()
                elif opcion == '7':
                    self.opcion_reporte_completo()
                else:
                    print("\n⚠️  Opción inválida. Intenta de nuevo.")
                
                if opcion != '0' and opcion != '7':
                    input("\n[Presiona ENTER para volver al menú...]")
                    
            except KeyboardInterrupt:
                print("\n\n👋 ¡Hasta luego!")
                break
            except Exception as e:
                print(f"\n❌ Error: {e}")
                input("\n[Presiona ENTER para continuar...]")


def main():
    """Punto de entrada principal."""
    app = VentasCLI()
    app.ejecutar()


if __name__ == '__main__':
    main()
