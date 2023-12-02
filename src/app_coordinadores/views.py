from django.shortcuts import render, get_object_or_404, redirect
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