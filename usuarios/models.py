from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    """Modelo de usuario personalizado con perfiles específicos"""
    
    PERFILES_CHOICES = [
        ('administrador', 'Administrador'),
        ('logistica', 'Logística'),
        ('inventario', 'Inventario'),
        ('auditor', 'Auditor'),
        ('comprador', 'Comprador'),
        ('produccion', 'Jefe de Producción'),
    ]
    
    perfil = models.CharField(
        max_length=20, 
        choices=PERFILES_CHOICES, 
        default='inventario',
        verbose_name='Perfil de acceso'
    )
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
    
    def __str__(self):
        return f"{self.username} ({self.get_perfil_display()})"
