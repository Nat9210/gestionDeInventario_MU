"""
Script para generar movimientos de entrada y salida de ejemplo
Ejecutar con: python manage.py shell < generar_movimientos_ejemplo.py
"""

from usuarios.models import Usuario
from inventario.models import Pieza, AlertaStock
from movimientos.models import MovimientoStock
from datetime import datetime, timedelta
import random

print("Generando movimientos de entrada y salida de ejemplo...")

# Obtener usuarios para asignar movimientos
try:
    user_logistica = Usuario.objects.get(username='logistica')
    user_inventario = Usuario.objects.get(username='inventario')
    user_admin = Usuario.objects.get(username='admin')
except Usuario.DoesNotExist:
    print("❌ Error: Usuarios no encontrados. Ejecuta primero cargar_datos_ejemplo.py")
    exit()

# Obtener todas las piezas
piezas = list(Pieza.objects.all())
if not piezas:
    print("❌ Error: No hay piezas en el sistema. Ejecuta primero cargar_datos_ejemplo.py")
    exit()

# Generar movimientos de los últimos 30 días
fecha_inicio = datetime.now() - timedelta(days=30)

movimientos_ejemplo = []

# 1. ENTRADAS DE COMPRAS (aumentan stock)
print("\n📥 Generando entradas de compras...")

entradas_compras = [
    {
        'codigo': 'ROD001',
        'cantidad': 50,
        'observaciones': 'Compra mensual a proveedor SKF',
        'usuario': user_logistica,
        'dias_atras': 25
    },
    {
        'codigo': 'TORN001', 
        'cantidad': 100,
        'observaciones': 'Reposición de stock crítico - Proveedor Aceros Unidos',
        'usuario': user_logistica,
        'dias_atras': 20
    },
    {
        'codigo': 'SEAL001',
        'cantidad': 15,
        'observaciones': 'Compra urgente por stock agotado',
        'usuario': user_admin,
        'dias_atras': 18
    },
    {
        'codigo': 'BELT001',
        'cantidad': 25,
        'observaciones': 'Entrada programada - Proveedor Gates',
        'usuario': user_logistica,
        'dias_atras': 15
    },
    {
        'codigo': 'FILT001',
        'cantidad': 20,
        'observaciones': 'Reposición filtros hidráulicos',
        'usuario': user_inventario,
        'dias_atras': 12
    },
    {
        'codigo': 'VALVE001',
        'cantidad': 10,
        'observaciones': 'Válvulas de repuesto para mantenimiento',
        'usuario': user_logistica,
        'dias_atras': 10
    },
    {
        'codigo': 'ELECT001',
        'cantidad': 8,
        'observaciones': 'Contactores para tablero eléctrico nuevo',
        'usuario': user_inventario,
        'dias_atras': 8
    }
]

for entrada in entradas_compras:
    try:
        pieza = Pieza.objects.get(codigo=entrada['codigo'])
        fecha = datetime.now() - timedelta(days=entrada['dias_atras'])
        
        movimiento = MovimientoStock.objects.create(
            pieza=pieza,
            tipo_movimiento='entrada',
            cantidad=entrada['cantidad'],
            observaciones=entrada['observaciones'],
            usuario=entrada['usuario']
        )
        # Ajustar la fecha manualmente
        MovimientoStock.objects.filter(id=movimiento.id).update(fecha_movimiento=fecha)
        
        print(f"✓ Entrada: {entrada['codigo']} (+{entrada['cantidad']}) - {entrada['observaciones'][:40]}...")
        
    except Pieza.DoesNotExist:
        print(f"❌ Pieza {entrada['codigo']} no encontrada")

# 2. SALIDAS POR CONSUMO (disminuyen stock)
print("\n📤 Generando salidas por consumo...")

salidas_consumo = [
    {
        'codigo': 'ROD001',
        'cantidad': 8,
        'observaciones': 'Mantenimiento motor bomba de agua Planta 1',
        'usuario': user_inventario,
        'dias_atras': 22
    },
    {
        'codigo': 'ROD001',
        'cantidad': 12,
        'observaciones': 'Reparación motores eléctricos - OT #2401',
        'usuario': user_logistica,
        'dias_atras': 14
    },
    {
        'codigo': 'TORN001',
        'cantidad': 45,
        'observaciones': 'Instalación estructura metálica nueva',
        'usuario': user_inventario,
        'dias_atras': 19
    },
    {
        'codigo': 'TORN001',
        'cantidad': 30,
        'observaciones': 'Mantenimiento preventivo equipos',
        'usuario': user_logistica,
        'dias_atras': 11
    },
    {
        'codigo': 'SEAL001',
        'cantidad': 3,
        'observaciones': 'Reparación bomba centrífuga Línea A',
        'usuario': user_inventario,
        'dias_atras': 16
    },
    {
        'codigo': 'SEAL001',
        'cantidad': 5,
        'observaciones': 'Mantenimiento bombas de proceso',
        'usuario': user_logistica,
        'dias_atras': 9
    },
    {
        'codigo': 'SEAL001',
        'cantidad': 7,
        'observaciones': 'Emergencia bomba principal - OT #2405',
        'usuario': user_admin,
        'dias_atras': 3
    },
    {
        'codigo': 'BELT001',
        'cantidad': 6,
        'observaciones': 'Cambio correas transmisión Sector B',
        'usuario': user_inventario,
        'dias_atras': 13
    },
    {
        'codigo': 'BELT001',
        'cantidad': 4,
        'observaciones': 'Mantenimiento ventiladores industriales',
        'usuario': user_logistica,
        'dias_atras': 7
    },
    {
        'codigo': 'FILT001',
        'cantidad': 8,
        'observaciones': 'Cambio filtros sistema hidráulico',
        'usuario': user_inventario,
        'dias_atras': 10
    },
    {
        'codigo': 'FILT001',
        'cantidad': 6,
        'observaciones': 'Mantenimiento preventivo prensas',
        'usuario': user_logistica,
        'dias_atras': 5
    },
    {
        'codigo': 'VALVE001',
        'cantidad': 3,
        'observaciones': 'Instalación nuevo sistema de vapor',
        'usuario': user_inventario,
        'dias_atras': 8
    },
    {
        'codigo': 'VALVE001',
        'cantidad': 2,
        'observaciones': 'Reparación línea de proceso química',
        'usuario': user_logistica,
        'dias_atras': 4
    },
    {
        'codigo': 'PIPE001',
        'cantidad': 2,
        'observaciones': 'Extensión red de aire comprimido',
        'usuario': user_inventario,
        'dias_atras': 6
    },
    {
        'codigo': 'ELECT001',
        'cantidad': 2,
        'observaciones': 'Instalación tablero control Línea C',
        'usuario': user_logistica,
        'dias_atras': 6
    },
    {
        'codigo': 'ELECT001',
        'cantidad': 3,
        'observaciones': 'Modernización sistema eléctrico',
        'usuario': user_inventario,
        'dias_atras': 2
    }
]

for salida in salidas_consumo:
    try:
        pieza = Pieza.objects.get(codigo=salida['codigo'])
        fecha = datetime.now() - timedelta(days=salida['dias_atras'])
        
        movimiento = MovimientoStock.objects.create(
            pieza=pieza,
            tipo_movimiento='salida',
            cantidad=salida['cantidad'],
            observaciones=salida['observaciones'],
            usuario=salida['usuario']
        )
        # Ajustar la fecha manualmente
        MovimientoStock.objects.filter(id=movimiento.id).update(fecha_movimiento=fecha)
        
        print(f"✓ Salida: {salida['codigo']} (-{salida['cantidad']}) - {salida['observaciones'][:40]}...")
        
    except Pieza.DoesNotExist:
        print(f"❌ Pieza {salida['codigo']} no encontrada")

# 3. DEVOLUCIONES (aumentan stock)
print("\n🔄 Generando devoluciones...")

devoluciones = [
    {
        'codigo': 'BELT001',
        'cantidad': 2,
        'observaciones': 'Devolución correas no utilizadas - OT #2398',
        'usuario': user_inventario,
        'dias_atras': 5
    },
    {
        'codigo': 'VALVE001',
        'cantidad': 1,
        'observaciones': 'Válvula en buen estado devuelta por cambio de especificación',
        'usuario': user_logistica,
        'dias_atras': 3
    }
]

for devolucion in devoluciones:
    try:
        pieza = Pieza.objects.get(codigo=devolucion['codigo'])
        fecha = datetime.now() - timedelta(days=devolucion['dias_atras'])
        
        movimiento = MovimientoStock.objects.create(
            pieza=pieza,
            tipo_movimiento='entrada',  # Devoluciones son entradas
            cantidad=devolucion['cantidad'],
            observaciones=devolucion['observaciones'],
            usuario=devolucion['usuario']
        )
        # Ajustar la fecha manualmente
        MovimientoStock.objects.filter(id=movimiento.id).update(fecha_movimiento=fecha)
        
        print(f"✓ Devolución: {devolucion['codigo']} (+{devolucion['cantidad']}) - {devolucion['observaciones'][:40]}...")
        
    except Pieza.DoesNotExist:
        print(f"❌ Pieza {devolucion['codigo']} no encontrada")

# 4. AJUSTES DE INVENTARIO
print("\n⚖️ Generando ajustes de inventario...")

ajustes = [
    {
        'codigo': 'PIPE001',
        'cantidad': 1,
        'observaciones': 'Ajuste por diferencia en conteo físico (+1)',
        'usuario': user_admin,
        'dias_atras': 1
    },
    {
        'codigo': 'FILT001',
        'cantidad': -2,
        'observaciones': 'Ajuste por filtros dañados en bodega (-2)',
        'usuario': user_inventario,
        'dias_atras': 1
    }
]

for ajuste in ajustes:
    try:
        pieza = Pieza.objects.get(codigo=ajuste['codigo'])
        fecha = datetime.now() - timedelta(days=ajuste['dias_atras'])
        
        tipo_mov = 'entrada' if ajuste['cantidad'] > 0 else 'salida'
        cantidad = abs(ajuste['cantidad'])
        
        movimiento = MovimientoStock.objects.create(
            pieza=pieza,
            tipo_movimiento=tipo_mov,
            cantidad=cantidad,
            observaciones=ajuste['observaciones'],
            usuario=ajuste['usuario']
        )
        # Ajustar la fecha manualmente
        MovimientoStock.objects.filter(id=movimiento.id).update(fecha_movimiento=fecha)
        
        signo = '+' if ajuste['cantidad'] > 0 else '-'
        print(f"✓ Ajuste: {ajuste['codigo']} ({signo}{cantidad}) - {ajuste['observaciones']}")
        
    except Pieza.DoesNotExist:
        print(f"❌ Pieza {ajuste['codigo']} no encontrada")

# Mostrar estadísticas finales
print(f"\n✅ Movimientos generados exitosamente!")
print(f"📊 Total de movimientos: {MovimientoStock.objects.count()}")
print(f"📥 Entradas: {MovimientoStock.objects.filter(tipo_movimiento='entrada').count()}")
print(f"📤 Salidas: {MovimientoStock.objects.filter(tipo_movimiento='salida').count()}")
print(f"🔄 Devoluciones: incluidas en entradas")
print(f"⚖️ Ajustes: incluidos en entradas/salidas")
print(f"⚠️ Alertas activas: {AlertaStock.objects.filter(activa=True).count()}")

print(f"\n📋 Stock actual de piezas después de movimientos:")
for pieza in Pieza.objects.all().order_by('codigo'):
    estado = "🔴 SIN STOCK" if pieza.stock_actual == 0 else "🟡 CRÍTICO" if pieza.stock_critico else "🟢 NORMAL"
    print(f"  {pieza.codigo}: {pieza.stock_actual} unidades - {estado}")

print(f"\n🎯 Para ver los movimientos en el sistema:")
print(f"   1. Inicia sesión con cualquier usuario")
print(f"   2. Ve a 'Movimientos' > 'Historial de Movimientos'")
print(f"   3. Ve a 'Inventario' > 'Alertas de Stock' para ver alertas críticas")
print(f"   4. Ve a cada pieza para ver su historial específico")
