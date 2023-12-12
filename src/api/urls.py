from django.urls import path
#from .views import CoordinadorListAPIView
from .import views

app_name = 'api'

urlpatterns = [
    path('coordinadores/', views.CoordinadorListAPIView.as_view(), name='listar_coordinadores'),
    path('empleados/', views.EmpleadosListAPIView.as_view(), name='listar_empleados'),
    path('empleados/<int:pk>', views.EmpleadosRetrieveAPIView.as_view(), name='buscar_empleado'),
]
