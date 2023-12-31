from django.urls import path
from . import views

app_name = 'app_empleados'

urlpatterns = [
    path('listado/', views.listado_empleados, name='listado_empleados'),
    path('modificar/<int:id>/', views.actualizar_empleado, name='actualizar_empleado'),
    path('nuevo/', views.EmpleadosCreateView.as_view(), name='registrar_empleado'),
    path('estado_activo/<int:id>', views.empleado_activo, name='estado_activo_empleado')
]
