from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_piezas, name='lista_piezas'),
    path('crear/', views.crear_pieza, name='crear_pieza'),
    path('editar/<int:pieza_id>/', views.editar_pieza, name='editar_pieza'),
    path('detalle/<int:pieza_id>/', views.detalle_pieza, name='detalle_pieza'),
    path('alertas/', views.alertas_stock, name='alertas_stock'),
]
