from django.urls import path
from .import views

app_name = 'app_servicios'

urlpatterns = [
    path('nuevo/', views.ServiciosCreateView.as_view(), name='registrar_servicio'),
    path('listado/', views.ServiciosListView.as_view(), name='lista_servicios'),
    path('modificar/<int:id>/', views.ServiciosUpdateView.as_view(), name='actualizar_servicio'),
    path('activar/<int:id>/', views.activar_servicio, name="activar_servicio"),
    path('desactivar/<int:id>/', views.desactivar_servicio, name="desactivar_servicio"),
]
