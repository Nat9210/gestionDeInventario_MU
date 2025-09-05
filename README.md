# Sistema de Inventario MVP - Maestranzas Unidas S.A.

Sistema web de gestión de inventario desarrollado con Django, diseñado para reemplazar el sistema manual basado en planillas de Maestranzas Unidas S.A.

## 🎯 Características Principales

### Sprint 1: Gestión y consulta de inventario + alertas
- ✅ **HU01.1** - Crear y editar usuarios con perfiles de acceso
- ✅ **HU03.1** - Registrar nueva pieza con código, descripción, stock y ubicación
- ✅ **HU03.2** - Editar datos de pieza existente
- ✅ **HU05** - Recibir alertas de stock crítico automáticas
- ✅ **HU17** - Login de usuarios con credenciales

### Sprint 2: Movimientos y control de stock
- ✅ **HU04** - Consultar piezas de inventario con filtros
- ✅ **HU07.1** - Registrar entrada de materiales
- ✅ **HU07.2** - Registrar salida de materiales

### Sprint 3: Trazabilidad y control
- ✅ **HU09.1** - Consultar stock actual de piezas individuales
- ✅ **HU11** - Consultar historial completo de movimientos

## 🚀 Inicio Rápido

### Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Instalación y Configuración

1. **Clonar o descargar el proyecto**
   ```bash
   # El proyecto ya está configurado en el directorio actual
   ```

2. **Activar el entorno virtual**
   ```bash
   # Windows
   .venv\Scripts\activate
   
   # Linux/Mac
   source .venv/bin/activate
   ```

3. **Instalar dependencias** (ya instaladas)
   ```bash
   pip install django django-crispy-forms crispy-bootstrap4
   ```

4. **Ejecutar migraciones** (ya aplicadas)
   ```bash
   python manage.py migrate
   ```

5. **Iniciar el servidor de desarrollo**
   ```bash
   python manage.py runserver
   ```

6. **Acceder al sistema**
   - URL: http://127.0.0.1:8000
   - Panel de administración: http://127.0.0.1:8000/admin

## 👥 Usuarios de Prueba

El sistema incluye usuarios de ejemplo con diferentes perfiles:

| Usuario     | Contraseña     | Perfil               | Permisos                                    |
|-------------|----------------|----------------------|---------------------------------------------|
| admin       | admin       | Administrador        | Acceso completo al sistema                  |
| logistica   | logistica123   | Logística           | Registro de entradas y salidas             |
| inventario  | inventario123  | Inventario          | Gestión de piezas y consultas              |
| comprador   | comprador123   | Comprador           | Visualización de alertas y consultas       |

## 📦 Datos de Ejemplo

El sistema incluye 8 piezas de ejemplo con diferentes estados de stock:
- **Piezas con stock normal**: ROD001, BELT001, VALVE001, PIPE001
- **Piezas con stock crítico**: TORN001, FILT001, ELECT001
- **Piezas sin stock**: SEAL001

## 🏗️ Estructura del Proyecto

```
GAP_MVP_MU/
├── inventario_mvp/          # Configuración principal del proyecto
├── usuarios/                # App de gestión de usuarios
├── inventario/              # App de gestión de piezas
├── movimientos/             # App de movimientos de stock
├── templates/               # Templates HTML
├── static/                  # Archivos estáticos (CSS, JS, imágenes)
├── manage.py               # Script de gestión de Django
└── db.sqlite3             # Base de datos SQLite
```

## 🔧 Funcionalidades Implementadas

### Autenticación y Usuarios
- Sistema de login seguro
- Gestión de usuarios con diferentes perfiles
- Control de permisos por perfil

### Gestión de Inventario
- Registro y edición de piezas
- Consulta con filtros avanzados
- Visualización del estado de stock
- Detalle completo de cada pieza

### Alertas Automáticas
- Generación automática de alertas por stock crítico
- Dashboard con resumen de alertas activas
- Notificaciones visuales por estado de stock

### Movimientos de Stock
- Registro de entradas de materiales
- Registro de salidas de materiales
- Actualización automática de stock tras cada transacción registrada
- Historial completo de movimientos

### Trazabilidad
- Historial detallado por pieza
- Registro de usuario que realizó cada movimiento
- Fechas y observaciones de cada operación

## 🎨 Tecnologías Utilizadas

- **Backend**: Django 5.2.3
- **Frontend**: Bootstrap 5.1.3 + Bootstrap Icons
- **Base de Datos**: SQLite (desarrollo)
- **Formularios**: Django Crispy Forms
- **Autenticación**: Sistema integrado de Django

## 🔒 Perfiles de Usuario

### Administrador
- Crear y editar usuarios
- Acceso completo a todas las funciones
- Gestión de piezas, movimientos y alertas

### Logística
- Registrar entradas y salidas de materiales
- Consultar inventario y alertas
- Ver historial de movimientos

### Inventario
- Gestionar piezas (crear y editar)
- Consultar inventario completo
- Ver alertas y movimientos

### Auditor
- Solo consulta y visualización
- Acceso al historial completo
- Sin permisos de modificación

### Comprador
- Ver alertas de stock crítico
- Consultar inventario
- Planificar reposiciones

### Jefe de Producción
- Consultar stock para planificación
- Ver disponibilidad de materiales
- Acceso a reportes

## 🚦 Estado del Proyecto

✅ **MVP Completado** - Todas las historias de usuario implementadas
- [x] Sprint 1: Gestión básica y alertas
- [x] Sprint 2: Movimientos y control
- [x] Sprint 3: Trazabilidad y completitud

## 📄 Próximos Pasos

Para evolucionar el sistema hacia una versión de producción:

1. **Seguridad**: Configurar HTTPS y variables de entorno
2. **Base de datos**: Migrar a PostgreSQL o MySQL
3. **Reportes**: Implementar reportes PDF y Excel
4. **Notificaciones**: Email automático para alertas críticas
5. **API**: Desarrollar API REST para integraciones
6. **Backup**: Sistema automático de respaldos

## 📞 Soporte

Para consultas sobre el sistema:
- Revisar la documentación en el código
- Consultar los comentarios en los modelos y vistas
- Verificar los templates para entender el flujo de usuario
