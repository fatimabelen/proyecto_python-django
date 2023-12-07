from django.urls import path
from .import views
app_name = 'app_servicios'

urlpatterns = [
    path('listado/', views.ServiciosListView.as_view(), name='listado_servicios'),
    path('modificar/<int:id>', views.ServiciosUpdateView.as_view(), name='actualizar_servicio'),
]
