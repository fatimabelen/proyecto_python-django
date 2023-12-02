from django.shortcuts import render
from .models import Empleado

# Create your views here.

def lista_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleados/lista_empleados.html', {'empleados': empleados})
