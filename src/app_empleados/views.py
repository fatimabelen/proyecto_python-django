from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .models import Empleado
from .forms import EmpleadoForm

# Create your views here.

def listado_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleados/lista_empleados.html', {'empleados': empleados})

# actualizacion de datos de empleados
def actualizar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)

    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('empleados:listado_empleados')

    else:
        form = EmpleadoForm(instance=empleado)

    return render(request, 'empleados/actualizar_empleado.html', {'form': form, 'empleado': empleado})