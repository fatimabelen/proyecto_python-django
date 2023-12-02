from django.urls import path
from . import views

app_name = 'coordinadores'

urlpatterns = [
    path('listado/', views.listado_coordinadores, name='listado_coordinadores'),
    path('modificar/<int:id>/', views.actualizar_coordinador, name='actualizar_coordinador')
]