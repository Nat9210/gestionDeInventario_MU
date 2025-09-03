from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.db import models
from .models import Usuario
from .forms import UsuarioForm, PerfilForm
from inventario.models import Pieza, AlertaStock
from movimientos.models import MovimientoStock


def es_administrador(user):
    """Verificar si el usuario es administrador"""
    return user.is_authenticated and user.perfil == 'administrador'


def logout_view(request):
    """Vista personalizada de logout que maneja GET y POST"""
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'Has cerrado sesión exitosamente.')
        return redirect('login')
    else:
        # Si es GET, mostrar confirmación
        return render(request, 'registration/logout_confirm.html')


@login_required
def dashboard(request):
    """Vista principal del dashboard"""
    # Estadísticas generales
    total_piezas = Pieza.objects.count()
    piezas_stock_critico = Pieza.objects.filter(
        stock_actual__lte=models.F('stock_minimo')
    ).count()
    alertas_activas = AlertaStock.objects.filter(activa=True).count()
    
    # Movimientos recientes
    movimientos_recientes = MovimientoStock.objects.select_related(
        'pieza', 'usuario'
    )[:10]
    
    # Piezas con stock crítico
    piezas_criticas = Pieza.objects.filter(
        stock_actual__lte=models.F('stock_minimo')
    )[:5]
    
    context = {
        'total_piezas': total_piezas,
        'piezas_stock_critico': piezas_stock_critico,
        'alertas_activas': alertas_activas,
        'movimientos_recientes': movimientos_recientes,
        'piezas_criticas': piezas_criticas,
    }
    
    return render(request, 'dashboard.html', context)


@user_passes_test(es_administrador)
def lista_usuarios(request):
    """Lista de usuarios (solo administradores)"""
    usuarios = Usuario.objects.all().order_by('username')
    return render(request, 'usuarios/lista.html', {'usuarios': usuarios})


@user_passes_test(es_administrador)
def crear_usuario(request):
    """Crear nuevo usuario (solo administradores)"""
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            messages.success(request, f'Usuario {usuario.username} creado exitosamente.')
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm()
    
    return render(request, 'usuarios/form.html', {
        'form': form,
        'titulo': 'Crear Usuario'
    })


@user_passes_test(es_administrador)
def editar_usuario(request, user_id):
    """Editar usuario existente (solo administradores)"""
    usuario = get_object_or_404(Usuario, id=user_id)
    
    if request.method == 'POST':
        form = PerfilForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, f'Usuario {usuario.username} actualizado exitosamente.')
            return redirect('lista_usuarios')
    else:
        form = PerfilForm(instance=usuario)
    
    return render(request, 'usuarios/form.html', {
        'form': form,
        'titulo': f'Editar Usuario: {usuario.username}'
    })
