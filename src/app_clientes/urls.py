from django.urls import path
from . import views

app_name = 'clientes'

urlpatterns = [
    path('listado/', views.listado_clientes, name='lista_clientes'),
    path('modificar/<int:id>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('activar/<int:pk>', views.ClienteUpdateView.as_view(), name='activar'),
    path('nuevo/', views.ClienteCreateView.as_view(), name='nuevo'),
   ]
