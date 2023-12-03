from django.urls import path
from app_coordinadores import views as coordinadores_views

app_name = 'empleados'

urlpatterns = [
    path('modificar/<int:id>/', coordinadores_views.actualizar_coordinador, name='actualizar_coordinador')
]