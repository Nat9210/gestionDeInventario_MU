from django.db import models
from django.contrib.auth import get_user_model
from inventario.models import Pieza

User = get_user_model()


class MovimientoStock(models.Model):
    """Modelo para registrar movimientos de entrada y salida"""
    
    TIPO_MOVIMIENTO_CHOICES = [
        ('entrada', 'Entrada'),
        ('salida', 'Salida'),
    ]
    
    pieza = models.ForeignKey(
        Pieza, 
        on_delete=models.CASCADE, 
        verbose_name='Pieza'
    )
    tipo_movimiento = models.CharField(
        max_length=10, 
        choices=TIPO_MOVIMIENTO_CHOICES, 
        verbose_name='Tipo de movimiento'
    )
    cantidad = models.PositiveIntegerField(verbose_name='Cantidad')
    fecha_movimiento = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='Fecha del movimiento'
    )
    usuario = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        verbose_name='Usuario que registró'
    )
    observaciones = models.TextField(
        blank=True, 
        verbose_name='Observaciones'
    )
    stock_anterior = models.PositiveIntegerField(
        verbose_name='Stock anterior'
    )
    stock_posterior = models.PositiveIntegerField(
        verbose_name='Stock posterior'
    )
    
    class Meta:
        verbose_name = 'Movimiento de Stock'
        verbose_name_plural = 'Movimientos de Stock'
        ordering = ['-fecha_movimiento']
    
    def __str__(self):
        return f"{self.get_tipo_movimiento_display()} - {self.pieza.codigo} - {self.cantidad}"
    
    def save(self, *args, **kwargs):
        """Sobrescribir save para actualizar el stock de la pieza"""
        # Guardar stock anterior
        self.stock_anterior = self.pieza.stock_actual
        
        # Actualizar stock según tipo de movimiento
        if self.tipo_movimiento == 'entrada':
            self.pieza.stock_actual += self.cantidad
        elif self.tipo_movimiento == 'salida':
            self.pieza.stock_actual = max(0, self.pieza.stock_actual - self.cantidad)
        
        # Guardar stock posterior
        self.stock_posterior = self.pieza.stock_actual
        
        # Guardar la pieza y el movimiento
        self.pieza.save()
        super().save(*args, **kwargs)
        
        # Verificar si necesita crear alerta de stock crítico
        self._verificar_alerta_stock()
    
    def _verificar_alerta_stock(self):
        """Crear alerta si el stock está crítico"""
        from inventario.models import AlertaStock
        
        if self.pieza.stock_critico:
            # Verificar si ya existe una alerta activa para esta pieza
            alerta_existente = AlertaStock.objects.filter(
                pieza=self.pieza, 
                activa=True
            ).exists()
            
            if not alerta_existente:
                AlertaStock.objects.create(pieza=self.pieza)
