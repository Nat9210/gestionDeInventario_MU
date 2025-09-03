from django.urls import path
from . import views

urlpatterns = [
    path('historial/', views.historial_movimientos, name='historial_movimientos'),
    path('entrada/', views.registrar_entrada, name='registrar_entrada'),
    path('salida/', views.registrar_salida, name='registrar_salida'),
    path('api/stock-pieza/', views.obtener_stock_pieza, name='obtener_stock_pieza'),
]
