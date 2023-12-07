from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .models import ReservaServicio


# Create your views here.

# Vista para crear nuevas reservas de servicios
class ReservasCreateView(generic.CreateView):
    model = ReservaServicio
    fields = '__all__'
    template_name = 'servicios/formulario_reservas.html'
    success_url = reverse_lazy('app_reservas:listado_reservas')
