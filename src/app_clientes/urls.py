from django.urls import path
from .import views

app_name = 'clientes'

urlpatterns = [
    path('/clientes/desactivar/<int:id>', views.desactivar_cliente, name='desactivar_cliente')
]
