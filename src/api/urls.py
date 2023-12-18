from django.urls import path
from .import views

app_name = 'api'

urlpatterns = [
    path('coordinadores/', views.CoordinadorListAPIView.as_view(), name='listar_coordinadores'),
    path('coordinadores/<int:pk>/', views.CoordinadorRetrieveAPIView.as_view(), name='buscar_coordinador'),
    path('empleados/', views.EmpleadoListAPIView.as_view(), name='listar_empleados'),
    path('empleados/<int:pk>', views.EmpleadoRetrieveAPIView.as_view(), name='buscar_empleado'),
    path('reservas/', views.ReservaListAPIView.as_view(), name='listar_reservas'),
    path('reservas/<int:pk>', views.ReservaRetrieveAPIView.as_view(), name='buscar_reserva'),
    path('clientes/', views.ClienteListAPIView.as_view(), name='listar_cliente'),
    path('clientes/<int:pk>/', views.ClienteRetrieveAPIView.as_view(), name='buscar_cliente'),
    path('servicios/', views.ServicioListAPIView.as_view(), name='listar_servicio'),
    path('servicios/<int:pk>/', views.ServicioRetrieveAPIView.as_view(), name='buscar_servicio'),
    path('documentacion/', views.api_documentacion, name='documentacion' )
]

