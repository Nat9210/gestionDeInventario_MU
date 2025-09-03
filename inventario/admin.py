from django.contrib import admin
from .models import Pieza, AlertaStock


@admin.register(Pieza)
class PiezaAdmin(admin.ModelAdmin):
    """Administrador para Pieza"""
    
    list_display = ('codigo', 'descripcion', 'stock_actual', 'stock_minimo', 'stock_critico', 'categoria', 'ubicacion')
    list_filter = ('categoria', 'fecha_creacion')
    search_fields = ('codigo', 'descripcion', 'categoria')
    ordering = ('codigo',)
    
    def stock_critico(self, obj):
        return obj.stock_critico
    stock_critico.boolean = True
    stock_critico.short_description = 'Stock Crítico'


@admin.register(AlertaStock)
class AlertaStockAdmin(admin.ModelAdmin):
    """Administrador para AlertaStock"""
    
    list_display = ('pieza', 'fecha_alerta', 'activa')
    list_filter = ('activa', 'fecha_alerta')
    search_fields = ('pieza__codigo', 'pieza__descripcion')
    ordering = ('-fecha_alerta',)
    readonly_fields = ('fecha_alerta',)
