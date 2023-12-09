from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic 
from django.urls import reverse_lazy
from .models import Empleado
from .forms import EmpleadoForm

# Create your views here.

# Listado de empleados
def listado_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleados/lista_empleados.html', {'empleados': empleados})


# Creación de nuevo empleado
class EmpleadosCreateView(generic.CreateView):
    model = Empleado
    fields = ['nombre', 'apellido', 'numero_legajo', 'activo']
    #exclude = ['activo']
    template_name = 'empleados/nuevo_empleado.html'
    extra_context = {'titulo':'REGISTRAR NUEVO EMPLEADO', 'mensaje_boton':'REGISTRAR EMPLEADO'}
    success_url = reverse_lazy('app_empleados:listado_empleados')

# actualizacion de datos de empleados
def actualizar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)

    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('app_empleados:listado_empleados')

    else:
        form = EmpleadoForm(instance=empleado)

    return render(request, 'empleados/actualizar_empleado.html', {'form': form, 'empleado': empleado})

"""# Activación del empleado
def activar_empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    empleado.activo = True
    empleado.save()
    return redirect('app_empleados:listado_empleados')

# Desactivación del empleado
def desactivar_empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    empleado.activo = False
    empleado.save()
    return redirect('app_empleados:listado_empleados')
"""
# Activar o desactivar un empleado
def empleado_activo(request, id):
    empleado = get_object_or_404(Empleado, id=id)

    if empleado.activo:
        empleado.activo = False
        empleado.save()
    else:
        empleado.activo = True
        empleado.save()

    return redirect('app_empleados:listado_empleados')