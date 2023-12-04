from django.contrib import admin
from .models import ReservaServicio
from app_clientes.models import Cliente
from app_coordinadores.models import Coordinador
from app_empleados.models import Empleado
from app_servicios.models import Servicio

# Register your models here.
@admin.register(ReservaServicio)
class ReservaServicioAdmin(admin.ModelAdmin):
    list_display = ['fecha_reserva', 'empleado', 'fecha_reservada', 'cliente', 'servicio', 'responsable']
    search_fields = ['cliente__nombre','cliente__apellido',  'servicio__nombre', 'empleado__nombre', 'empleado__apellido', 'responsable__nombre', 'responsable__apellido']



