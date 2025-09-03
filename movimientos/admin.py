from django.contrib import admin
from .models import MovimientoStock


@admin.register(MovimientoStock)
class MovimientoStockAdmin(admin.ModelAdmin):
    """Administrador para MovimientoStock"""
    
    list_display = ('pieza', 'tipo_movimiento', 'cantidad', 'fecha_movimiento', 'usuario', 'stock_anterior', 'stock_posterior')
    list_filter = ('tipo_movimiento', 'fecha_movimiento', 'usuario')
    search_fields = ('pieza__codigo', 'pieza__descripcion', 'observaciones')
    ordering = ('-fecha_movimiento',)
    readonly_fields = ('fecha_movimiento', 'stock_anterior', 'stock_posterior')
    
    def has_change_permission(self, request, obj=None):
        # No permitir editar movimientos una vez creados
        return False
