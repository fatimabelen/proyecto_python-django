from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .models import Servicio


# Create your views here.

# Vista para listar los servicios
class ServiciosListView(generic.ListView):
    model = Servicio
    fields = '__all__'
    template_name = 'servicios/listado_servicios.html'
    context_object_name = 'servicios'


# Vista para actualizar un registro de servicio
class ServiciosUpdateView(generic.UpdateView):
    model = Servicio
    fields = ['nombre', 'descripcion', 'precio']
    template_name = 'servicios/formulario_servicios.html'
    success_url = reverse_lazy('app_servicios:listado_servicios')
    
