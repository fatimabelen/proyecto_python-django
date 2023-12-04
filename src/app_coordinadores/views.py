from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy
from .models import Coordinador
from .forms import CoordinadorForm

# Create your views here.

# mostrar la lista de coordinadores
def listado_coordinadores(request):
    coordinadores = Coordinador.objects.all()
    return render(request, 'coordinadores/lista_coordinadores.html', {'coordinadores': coordinadores})


# actualizacion de datos de coordinadores
def actualizar_coordinador(request, id):
    coordinador = get_object_or_404(Coordinador, id=id)

    if request.method == 'POST':
        form = CoordinadorForm(request.POST, instance=coordinador)
        if form.is_valid():
            form.save()
            return redirect('coordinadores:listado_coordinadores')

    else:
        form = CoordinadorForm(instance=coordinador)

    return render(request, 'coordinadores/actualizar_coordinador.html', {'form': form, 'coordinador': coordinador})


class CoordinadorCreateView(generic.CreateView):
    model = 'Coordinador'
    fields = ['nombre', 'apellido', 'numero_documento', 'fecha_alta']
    template_name = 'app_coordinadores/nuevo_coordinador.html'
    success_url = reverse_lazy('coordinadores:listado_coordinadores')


# Vista para activar el registro de un coordinador
def activar_coordinador(request, id):
    coordinador = get_object_or_404(Coordinador, id=id)
    coordinador.activo = True
    coordinador.save()  # Guarda los cambios en la base de datos
    mensaje = f'El registro del coordinador se activó con éxito.'

    # Falta el return

