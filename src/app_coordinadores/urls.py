from django.urls import path
from .import views

app_name = 'app_coordinadores'

urlpatterns = [
   
    path('listado/', views.listado_coordinadores, name='listado_coordinadores'),
    path('modificar/<int:id>/', views.actualizar_coordinador, name='actualizar_coordinador'),
    path('nuevo/', views.CoordinadorCreateView.as_view(), name='crear_coordinador'),
    path('activar/<int:id>/', views.activar_coordinador, name='activar_coordinador'),
    path('desactivar/<int:id>', views.desactivar_coordinador, name='desactivar_coordinador'),
]
