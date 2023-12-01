from django.contrib import admin
from .models import ReservaServicio

# Register your models here.
@admin.register(ReservaServicio)
class ReservaServicioAdmin(admin.ModelAdmin):
    list_display = ['fecha_reserva', 'empleado', 'fecha_reservada', 'cliente', 'servicio', 'responsable']



