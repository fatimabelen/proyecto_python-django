from django.urls import path
from .import views

app_name = 'coordinadores'

urlpatterns = [
   
    path('listado/', views.listado_coordinadores, name='listado_coordinadores'),
    path('modificar/<int:id>/', views.actualizar_coordinador, name='actualizar_coordinador'),
    path('coordinadores/nuevo', views.CoordinadorCreateView.as_view(), name='crear_coordinador'),
    path('coordinadores/activar/<int:id>/', views.activar_coordinador, name='activar_coordinador'),
]
