from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from .models import Coordinador

# Create your views here.

class CoordinadorCreateView(generic.CreateView):
    model = 'Coordinador'
    fields = ['nombre', 'apellido', 'numero_documento', 'fecha_alta']
    template_name = 'app_coordinadores/nuevo_coordinador.html'
    success_url = reverse_lazy('coordinadores:listado_coordinadores')

def activar_coordinador(request, id):
    coordinador = get_object_or_404(Coordinador, id=id)
    coordinador.activo = True
    coordinador.save()
    mensaje = f'El registro del coordinador se activó con éxito.'

    return render(request, 'coordinadores:activar_coordinador', {'mensaje':mensaje})
