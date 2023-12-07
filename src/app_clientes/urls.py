from django.urls import path
from . import views

app_name = 'clientes'

urlpatterns = [
    path('listado/', views.listado_clientes, name='listado_clientes'),
    path('nuevo/', views.ClientesCreateView.as_view(), name="registrar_cliente"),
    #path('modificar/<int:pk>/', views.ClientesUpdateView.as_view(), name="actualizar_cliente"),
    path('modificar/<int:id>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('desactivar/<int:id>', views.desactivar_cliente, name='desactivar_cliente'),
    path('activar/<int:id>', views.activar_cliente, name="activar_cliente"),
]
