from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib import messages
from .models import Servicio
from .forms import ServicioUpdateForm

# Create your views here.

# Registrar nuevos servicios
class ServiciosCreateView(generic.CreateView):
    model = Servicio
    form_class = ServicioUpdateForm
    template_name = 'servicios/formulario_servicios.html'
    extra_context = {'titulo': 'REGISTRAR SERVICIO', 'mensaje_boton':'REGISTRAR SERVICIO'}
    success_url = reverse_lazy('app_servicios:listado_servicios')

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)
    

# Listar los servicios
class ServiciosListView(generic.ListView):
    model = Servicio
    fields = '__all__'
    template_name = 'servicios/lista_servicios.html'
    context_object_name = 'servicios'


# Actualizar un registro de servicio

class ServiciosUpdateView(generic.UpdateView):
    model = Servicio
    fields = ['nombre', 'descripcion', 'precio']
    template_name = 'servicios/formulario_servicios.html'
    extra_context = {'titulo' : 'ACTUALIZAR SERVICIO', 'mensaje_boton' : 'ACTUALIZAR SERVICIO'}
    success_url = reverse_lazy('app_servicios:listado_servicios')


# Activar el registro de un servicio
def activar_servicio(request, id):
    servicio = get_object_or_404(Servicio, id=id)
    servicio.activo = True
    servicio.save()
    return redirect('app_servicios:listado_servicios')


# Desactivar el registro de un servicio
def desactivar_servicio(request, id):
    servicio = get_object_or_404(Servicio, id=id)
    servicio.activo = False
    servicio.save()
    return redirect('app_servicios:listado_servicios')    