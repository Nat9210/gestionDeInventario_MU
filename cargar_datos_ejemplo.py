"""
Script para cargar datos de ejemplo en el sistema
Ejecutar con: python manage.py shell < cargar_datos_ejemplo.py
"""

from usuarios.models import Usuario
from inventario.models import Pieza, AlertaStock
from movimientos.models import MovimientoStock
from django.contrib.auth import get_user_model

# Crear usuarios de ejemplo
print("Creando usuarios de ejemplo...")

# Usuario administrador (si no existe ya)
if not Usuario.objects.filter(username='admin').exists():
    admin = Usuario.objects.create_user(
        username='admin',
        email='admin@maestranzas.cl',
        password='admin123',
        first_name='Administrador',
        last_name='Sistema',
        perfil='administrador',
        is_staff=True,
        is_superuser=True
    )
    print(f"✓ Usuario administrador creado: {admin.username}")

# Usuario de logística
if not Usuario.objects.filter(username='logistica').exists():
    logistica = Usuario.objects.create_user(
        username='logistica',
        email='logistica@maestranzas.cl',
        password='logistica123',
        first_name='Carlos',
        last_name='Pérez',
        perfil='logistica'
    )
    print(f"✓ Usuario logística creado: {logistica.username}")

# Usuario de inventario
if not Usuario.objects.filter(username='inventario').exists():
    inventario = Usuario.objects.create_user(
        username='inventario',
        email='inventario@maestranzas.cl',
        password='inventario123',
        first_name='María',
        last_name='González',
        perfil='inventario'
    )
    print(f"✓ Usuario inventario creado: {inventario.username}")

# Usuario comprador
if not Usuario.objects.filter(username='comprador').exists():
    comprador = Usuario.objects.create_user(
        username='comprador',
        email='comprador@maestranzas.cl',
        password='comprador123',
        first_name='Juan',
        last_name='Rodríguez',
        perfil='comprador'
    )
    print(f"✓ Usuario comprador creado: {comprador.username}")

# Crear piezas de ejemplo
print("\nCreando piezas de ejemplo...")

piezas_ejemplo = [
    {
        'codigo': 'ROD001',
        'descripcion': 'Rodamiento 6201-2RS para motor eléctrico',
        'stock_actual': 25,
        'stock_minimo': 10,
        'ubicacion': 'Estante A-1',
        'categoria': 'Rodamientos'
    },
    {
        'codigo': 'TORN001',
        'descripcion': 'Tornillo hexagonal M8x30 acero inoxidable',
        'stock_actual': 5,  # Stock crítico
        'stock_minimo': 20,
        'ubicacion': 'Gaveta B-15',
        'categoria': 'Tornillería'
    },
    {
        'codigo': 'SEAL001',
        'descripcion': 'Sello mecánico para bomba centrífuga 25mm',
        'stock_actual': 0,  # Sin stock
        'stock_minimo': 5,
        'ubicacion': 'Estante C-3',
        'categoria': 'Sellos'
    },
    {
        'codigo': 'BELT001',
        'descripcion': 'Correa trapecial A50 para transmisión',
        'stock_actual': 15,
        'stock_minimo': 8,
        'ubicacion': 'Estante D-2',
        'categoria': 'Correas'
    },
    {
        'codigo': 'FILT001',
        'descripcion': 'Filtro de aceite hidráulico 10 micrones',
        'stock_actual': 3,  # Stock crítico
        'stock_minimo': 6,
        'ubicacion': 'Estante E-1',
        'categoria': 'Filtros'
    },
    {
        'codigo': 'VALVE001',
        'descripcion': 'Válvula de bola 1/2" acero inoxidable',
        'stock_actual': 12,
        'stock_minimo': 5,
        'ubicacion': 'Estante F-4',
        'categoria': 'Válvulas'
    },
    {
        'codigo': 'PIPE001',
        'descripcion': 'Tubería de cobre 1/2" x 3 metros',
        'stock_actual': 8,
        'stock_minimo': 4,
        'ubicacion': 'Rack G-1',
        'categoria': 'Tuberías'
    },
    {
        'codigo': 'ELECT001',
        'descripcion': 'Contactor 3 polos 25A 220V',
        'stock_actual': 1,  # Stock crítico
        'stock_minimo': 3,
        'ubicacion': 'Estante H-2',
        'categoria': 'Eléctricos'
    }
]

for pieza_data in piezas_ejemplo:
    if not Pieza.objects.filter(codigo=pieza_data['codigo']).exists():
        pieza = Pieza.objects.create(**pieza_data)
        print(f"✓ Pieza creada: {pieza.codigo} - {pieza.descripcion[:30]}...")
        
        # Crear alerta si el stock está crítico
        if pieza.stock_critico:
            AlertaStock.objects.create(pieza=pieza)
            print(f"  ⚠️ Alerta de stock crítico creada para {pieza.codigo}")

print(f"\n✅ Datos de ejemplo cargados exitosamente!")
print(f"📊 Total de usuarios: {Usuario.objects.count()}")
print(f"📦 Total de piezas: {Pieza.objects.count()}")
print(f"⚠️ Total de alertas: {AlertaStock.objects.filter(activa=True).count()}")

print("\n🔑 Credenciales de acceso:")
print("👤 Administrador: admin / admin123")
print("📋 Logística: logistica / logistica123") 
print("📊 Inventario: inventario / inventario123")
print("🛒 Comprador: comprador / comprador123")
