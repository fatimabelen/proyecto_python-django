from django.urls import path
from .import views

app_name = 'app_reservas'

urlpatterns = [
    path('nuevo/', views.ReservasCreateView.as_view(), name='registrar_reserva'),
    path('modificar/<int:pk>/', views.editar_reserva, name='actualizar_reserva'),
    path('eliminar/<int:pk>/', views.ReservaServicioDeleteView.as_view(), name='eliminar_reserva')
]


