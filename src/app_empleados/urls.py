from django.urls import path
from . import views
from app_coordinadores import views

app_name = 'empleados'

urlpatterns = [
    path('modificar/<int:id>/', views.actualizar_coordinador, name='actualizar_coordinador')
]