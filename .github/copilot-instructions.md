<!-- Use this file to provide workspace-specific custom instructions to Copilot. For more details, visit https://code.visualstudio.com/docs/copilot/copilot-customization#_use-a-githubcopilotinstructionsmd-file -->

# Sistema de Inventario MVP - Maestranzas Unidas

## Contexto del Proyecto
Este es un MVP (Producto Mínimo Viable) de un sistema de gestión de inventario desarrollado con Django para Maestranzas Unidas S.A. El objetivo es reemplazar un sistema manual basado en planillas de papel.

## Arquitectura del Sistema

### Aplicaciones Django
- **usuarios**: Gestión de usuarios con perfiles específicos (administrador, logística, inventario, auditor, comprador, producción)
- **inventario**: Gestión de piezas, stock y alertas automáticas
- **movimientos**: Registro de entradas y salidas de materiales con trazabilidad completa

### Modelos Principales
- **Usuario**: Extiende AbstractUser con campo `perfil` para control de permisos
- **Pieza**: Código único, descripción, stock actual/mínimo, ubicación, categoría
- **MovimientoStock**: Entradas/salidas con actualización automática de stock
- **AlertaStock**: Alertas automáticas por stock crítico

### Tecnologías Utilizadas
- Django 5.2.3 con autenticación integrada
- Bootstrap 5.1.3 para UI responsiva
- Django Crispy Forms para formularios
- SQLite para desarrollo (preparado para PostgreSQL en producción)

## Convenciones de Código

### Nomenclatura
- Modelos en singular y PascalCase: `Pieza`, `MovimientoStock`
- Variables y funciones en snake_case: `stock_actual`, `crear_pieza`
- Templates en kebab-case: `lista-piezas.html`
- URLs descriptivas: `inventario/crear/`, `movimientos/entrada/`

### Permisos y Seguridad
- Decoradores `@login_required` para todas las vistas
- Funciones `user_passes_test()` para control por perfil
- Validación de permisos en templates con `{% if user.perfil in '...' %}`

### Patrones de Desarrollo
- Vistas basadas en funciones (no CBV)
- Formularios Django con validaciones personalizadas
- Templates que extienden `base.html`
- Mensajes flash para feedback al usuario
- Filtros de búsqueda en todas las listas

## Funcionalidades Específicas

### Alertas Automáticas
- Se crean automáticamente cuando `stock_actual <= stock_minimo`
- Se desactivan cuando el stock supera el mínimo
- Visibles en dashboard y página específica de alertas

### Actualización de Stock
- Los movimientos actualizan automáticamente el stock en el método `save()`
- Se registra stock anterior y posterior para trazabilidad
- Validación para evitar stock negativo en salidas

### Control de Permisos por Perfil
- **Administrador**: Acceso completo
- **Logística**: Registrar entradas/salidas
- **Inventario**: Gestionar piezas y consultas
- **Auditor**: Solo lectura y trazabilidad
- **Comprador**: Ver alertas y consultas
- **Producción**: Consultas para planificación

## Patrones de UI/UX

### Colores y Estados
- Verde: Stock normal, entradas, éxito
- Amarillo/Naranja: Stock crítico, advertencias
- Rojo: Sin stock, salidas, errores
- Azul: Información, navegación
- Gris: Elementos deshabilitados o sin datos

### Iconografía Bootstrap Icons
- `bi-boxes`: Inventario general
- `bi-arrow-down-circle`: Entradas
- `bi-arrow-up-circle`: Salidas  
- `bi-exclamation-triangle`: Alertas
- `bi-clock-history`: Historial
- `bi-people`: Usuarios

### Navegación
- Sidebar persistente para usuarios autenticados
- Breadcrumbs en formularios con botón "Volver"
- Filtros expansibles en listas
- Paginación cuando sea necesario

## Consideraciones para Desarrollo

### Al agregar nuevas funcionalidades:
1. Mantener consistencia con perfiles de usuario existentes
2. Usar templates existentes como base
3. Implementar validaciones tanto en formularios como en modelos
4. Agregar pruebas unitarias para lógica crítica
5. Documentar cambios en README.md

### Al modificar modelos:
1. Crear migraciones inmediatamente: `python manage.py makemigrations`
2. Aplicar migraciones: `python manage.py migrate`
3. Actualizar admin.py si es necesario
4. Verificar impacto en formularios y vistas relacionadas

### Debugging y Testing:
- Usar `python manage.py shell` para pruebas de modelos
- Panel de admin en `/admin/` para verificación de datos
- Datos de ejemplo cargados con `cargar_datos_ejemplo.py`
- Logs de Django habilitados en desarrollo

### Assets Estáticos:
- **CSS personalizado**: `static/css/inventario.css` con variables CSS y componentes reutilizables
- **JavaScript**: `static/js/inventario.js` con módulos para gestión de stock, filtros y formularios
- **Funcionalidades JS**: AJAX, validación en tiempo real, filtros dinámicos, notificaciones toast
- **Herramientas**: Fetch API, debounce, animaciones CSS, gestión de estado

Este sistema está diseñado para ser mantenible, escalable y fácil de entender para desarrolladores que trabajen en el futuro.
