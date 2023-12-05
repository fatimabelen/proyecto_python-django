from django.urls import path
from . import views

app_name = 'clientes'

urlpatterns = [
    #path('listado/', views.listado_clientes, name='listado_clientes'),
    path('listado/', views.ClientesListView.as_view(), name='listar_clientes'),
    #path('clientes/desactivar/<int:id>', views.desactivar_cliente, name='desactivar_cliente')
]
