from django.contrib import admin
from .models import Empleado
# Register your models here.
@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ['apellido', 'nombre', 'numero_legajo', 'activo']
    list_filter = ['activo']
    search_fields = ['apellido', 'nombre']
   