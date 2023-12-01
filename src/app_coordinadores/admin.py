from django.contrib import admin
from .models import Coordinador

# Register your models here.

@admin.register(Coordinador)
class CoordinadorAdmin(admin.ModelAdmin):
    list_display = ['apellido', 'nombre', 'número_documento', 'fecha_alta', 'activo']
    search_fields =  ['apellido', 'nombre']
    list_filter = ['activo']