from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    """Administrador personalizado para Usuario"""
    
    fieldsets = UserAdmin.fieldsets + (
        ('Perfil Personalizado', {'fields': ('perfil',)}),
    )
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Perfil Personalizado', {'fields': ('perfil',)}),
    )
    
    list_display = ('username', 'email', 'first_name', 'last_name', 'perfil', 'is_active', 'is_staff')
    list_filter = ('perfil', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('username', 'first_name', 'last_name', 'email')
