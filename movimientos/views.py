from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from .models import MovimientoStock
from .forms import MovimientoForm
from inventario.models import Pieza


def es_logistica_o_admin(user):
    """Verificar si el usuario puede registrar movimientos"""
    return user.is_authenticated and user.perfil in ['administrador', 'logistica']


@login_required
def historial_movimientos(request):
    """Historial completo de movimientos"""
    movimientos = MovimientoStock.objects.select_related('pieza', 'usuario').all()
    
    # Filtros
    busqueda = request.GET.get('busqueda', '')
    tipo_movimiento = request.GET.get('tipo_movimiento', '')
    fecha_desde = request.GET.get('fecha_desde', '')
    fecha_hasta = request.GET.get('fecha_hasta', '')
    
    if busqueda:
        movimientos = movimientos.filter(
            Q(pieza__codigo__icontains=busqueda) | 
            Q(pieza__descripcion__icontains=busqueda) |
            Q(observaciones__icontains=busqueda)
        )
    
    if tipo_movimiento:
        movimientos = movimientos.filter(tipo_movimiento=tipo_movimiento)
    
    if fecha_desde:
        movimientos = movimientos.filter(fecha_movimiento__date__gte=fecha_desde)
    
    if fecha_hasta:
        movimientos = movimientos.filter(fecha_movimiento__date__lte=fecha_hasta)
    
    movimientos = movimientos.order_by('-fecha_movimiento')
    
    context = {
        'movimientos': movimientos,
        'busqueda': busqueda,
        'tipo_movimiento_filtro': tipo_movimiento,
        'fecha_desde': fecha_desde,
        'fecha_hasta': fecha_hasta,
    }
    
    return render(request, 'movimientos/historial.html', context)


@user_passes_test(es_logistica_o_admin)
def registrar_entrada(request):
    """Registrar entrada de materiales"""
    if request.method == 'POST':
        form = MovimientoForm(request.POST, tipo_movimiento='entrada')
        if form.is_valid():
            movimiento = form.save(commit=False)
            movimiento.usuario = request.user
            movimiento.tipo_movimiento = 'entrada'
            movimiento.save()
            messages.success(
                request, 
                f'Entrada registrada: {movimiento.cantidad} unidades de {movimiento.pieza.codigo}'
            )
            return redirect('lista_piezas')
    else:
        form = MovimientoForm(tipo_movimiento='entrada')
    
    return render(request, 'movimientos/form.html', {
        'form': form,
        'titulo': 'Registrar Entrada de Materiales',
        'tipo': 'entrada'
    })


@user_passes_test(es_logistica_o_admin)
def registrar_salida(request):
    """Registrar salida de materiales"""
    if request.method == 'POST':
        form = MovimientoForm(request.POST, tipo_movimiento='salida')
        if form.is_valid():
            movimiento = form.save(commit=False)
            movimiento.usuario = request.user
            movimiento.tipo_movimiento = 'salida'
            
            # Verificar que hay suficiente stock
            if movimiento.cantidad > movimiento.pieza.stock_actual:
                messages.error(
                    request, 
                    f'Stock insuficiente. Stock actual: {movimiento.pieza.stock_actual}'
                )
                return render(request, 'movimientos/form.html', {
                    'form': form,
                    'titulo': 'Registrar Salida de Materiales',
                    'tipo': 'salida'
                })
            
            movimiento.save()
            messages.success(
                request, 
                f'Salida registrada: {movimiento.cantidad} unidades de {movimiento.pieza.codigo}'
            )
            return redirect('lista_piezas')
    else:
        form = MovimientoForm(tipo_movimiento='salida')
    
    return render(request, 'movimientos/form.html', {
        'form': form,
        'titulo': 'Registrar Salida de Materiales',
        'tipo': 'salida'
    })


@login_required
def obtener_stock_pieza(request):
    """API para obtener el stock actual de una pieza"""
    pieza_id = request.GET.get('pieza_id')
    if pieza_id:
        try:
            pieza = Pieza.objects.get(id=pieza_id)
            return JsonResponse({
                'stock_actual': pieza.stock_actual,
                'codigo': pieza.codigo,
                'descripcion': pieza.descripcion
            })
        except Pieza.DoesNotExist:
            return JsonResponse({'error': 'Pieza no encontrada'}, status=404)
    
    return JsonResponse({'error': 'ID de pieza requerido'}, status=400)
