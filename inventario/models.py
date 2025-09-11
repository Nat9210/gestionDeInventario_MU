from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Pieza(models.Model):
    """Modelo para las piezas del inventario"""
    
    codigo = models.CharField(
        max_length=50, 
        unique=True, 
        verbose_name='Código de pieza'
    )
    descripcion = models.TextField(verbose_name='Descripción')
    stock_actual = models.PositiveIntegerField(
        default=0, 
        verbose_name='Stock actual'
    )
    stock_minimo = models.PositiveIntegerField(
        default=10, 
        verbose_name='Stock mínimo'
    )
    ubicacion = models.CharField(
        max_length=100, 
        verbose_name='Ubicación en bodega'
    )
    categoria = models.CharField(
        max_length=50, 
        blank=True, 
        verbose_name='Categoría'
    )
    fecha_creacion = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='Fecha de creación'
    )
    fecha_actualizacion = models.DateTimeField(
        auto_now=True, 
        verbose_name='Última actualización'
    )
    ultima_modificacion_por = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name='Última modificación por'
    )
    fecha_ultima_modificacion = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Fecha de última modificación'
    )
    
    class Meta:
        verbose_name = 'Pieza'
        verbose_name_plural = 'Piezas'
        ordering = ['codigo']
    
    def __str__(self):
        return f"{self.codigo} - {self.descripcion}"
    
    @property
    def stock_critico(self):
        """Indica si el stock está por debajo del mínimo"""
        return self.stock_actual <= self.stock_minimo
    
    @property
    def estado_stock(self):
        """Devuelve el estado del stock"""
        if self.stock_actual == 0:
            return 'Sin stock'
        elif self.stock_critico:
            return 'Stock crítico'
        else:
            return 'Stock normal'


class AlertaStock(models.Model):
    """Modelo para las alertas de stock crítico"""
    
    pieza = models.ForeignKey(
        Pieza, 
        on_delete=models.CASCADE, 
        verbose_name='Pieza'
    )
    fecha_alerta = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='Fecha de alerta'
    )
    activa = models.BooleanField(
        default=True, 
        verbose_name='Alerta activa'
    )
    vista_por = models.ManyToManyField(
        User, 
        blank=True, 
        verbose_name='Vista por usuarios'
    )
    
    class Meta:
        verbose_name = 'Alerta de Stock'
        verbose_name_plural = 'Alertas de Stock'
        ordering = ['-fecha_alerta']
    
    def __str__(self):
        return f"Alerta: {self.pieza.codigo} - Stock: {self.pieza.stock_actual}"
