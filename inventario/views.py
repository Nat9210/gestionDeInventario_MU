from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.db.models import Q, F
from django.http import JsonResponse
from .models import Pieza, AlertaStock
from .forms import PiezaForm
from movimientos.models import MovimientoStock


def es_gestor_o_admin(user):
    """Verificar si el usuario puede gestionar inventario"""
    return user.is_authenticated and user.perfil in ['administrador', 'inventario', 'logistica']


@login_required
def lista_piezas(request):
    """Lista de piezas con filtros"""
    piezas = Pieza.objects.all()
    
    # Filtros
    busqueda = request.GET.get('busqueda', '')
    categoria = request.GET.get('categoria', '')
    estado_stock = request.GET.get('estado_stock', '')
    
    if busqueda:
        piezas = piezas.filter(
            Q(codigo__icontains=busqueda) | 
            Q(descripcion__icontains=busqueda)
        )
    
    if categoria:
        piezas = piezas.filter(categoria__icontains=categoria)
    
    if estado_stock == 'critico':
        piezas = piezas.filter(stock_actual__lte=F('stock_minimo'))
    elif estado_stock == 'sin_stock':
        piezas = piezas.filter(stock_actual=0)
    elif estado_stock == 'normal':
        piezas = piezas.filter(stock_actual__gt=F('stock_minimo'))
    
    # Obtener categorías únicas para el filtro
    categorias = Pieza.objects.values_list('categoria', flat=True).distinct()
    
    piezas = piezas.order_by('codigo')
    
    context = {
        'piezas': piezas,
        'categorias': categorias,
        'busqueda': busqueda,
        'categoria_filtro': categoria,
        'estado_stock_filtro': estado_stock,
    }
    
    return render(request, 'inventario/lista.html', context)


@user_passes_test(es_gestor_o_admin)
def crear_pieza(request):
    """Crear nueva pieza"""
    if request.method == 'POST':
        form = PiezaForm(request.POST)
        if form.is_valid():
            pieza = form.save()
            messages.success(request, f'Pieza {pieza.codigo} creada exitosamente.')
            return redirect('lista_piezas')
    else:
        form = PiezaForm()
    
    return render(request, 'inventario/form.html', {
        'form': form,
        'titulo': 'Registrar Nueva Pieza'
    })


@user_passes_test(es_gestor_o_admin)
def editar_pieza(request, pieza_id):
    """Editar pieza existente"""
    pieza = get_object_or_404(Pieza, id=pieza_id)
    
    if request.method == 'POST':
        form = PiezaForm(request.POST, instance=pieza)
        if form.is_valid():
            form.save()
            messages.success(request, f'Pieza {pieza.codigo} actualizada exitosamente.')
            return redirect('lista_piezas')
    else:
        form = PiezaForm(instance=pieza)
    
    return render(request, 'inventario/form.html', {
        'form': form,
        'titulo': f'Editar Pieza: {pieza.codigo}'
    })


@login_required
def detalle_pieza(request, pieza_id):
    """Ver detalle de una pieza y su historial"""
    pieza = get_object_or_404(Pieza, id=pieza_id)
    movimientos = MovimientoStock.objects.filter(pieza=pieza).order_by('-fecha_movimiento')[:20]
    
    context = {
        'pieza': pieza,
        'movimientos': movimientos,
    }
    
    return render(request, 'inventario/detalle.html', context)


@login_required
def alertas_stock(request):
    """Ver alertas de stock crítico"""
    alertas = AlertaStock.objects.filter(activa=True).select_related('pieza')
    
    # Marcar alerta como vista por el usuario actual
    if request.method == 'POST':
        alerta_id = request.POST.get('alerta_id')
        if alerta_id:
            alerta = get_object_or_404(AlertaStock, id=alerta_id)
            alerta.vista_por.add(request.user)
            return JsonResponse({'status': 'success'})
    
    context = {
        'alertas': alertas,
    }
    
    return render(request, 'inventario/alertas.html', context)
