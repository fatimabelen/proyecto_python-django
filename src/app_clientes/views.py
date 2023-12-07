from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.http import HttpResponse
from .forms import ClienteUpdateForm
from .models import Cliente

# Create your views here.
def listado_clientes(request):
   clientes = Cliente.objects.all()
   return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})


# Crear nuevo cliente
class ClientesCreateView(generic.CreateView):
    model = Cliente
    fields = ['nombre', 'apellido']
    template_name = 'clientes/formulario_clientes.html'
    extra_context = {'titulo':'REGISTRAR CLIENTE', 'mensaje_boton':'REGISTRAR CLIENTE'}
    success_url = reverse_lazy('clientes:listado_clientes')

"""
# Actualizar cliente
class ClientesUpdateView(generic.UpdateView):
    model = Cliente
    fields =  ['nombre', 'apellido']
    template_name = 'clientes/formulario_clientes.html'
    extra_context = {'titulo':'ACTUALIZAR CLIENTE', 'mensaje_boton':'ACTUALIZAR CLIENTE'}
    success_url = reverse_lazy('clientes:listado_clientes')
"""

# actualizacion de datos de clientes
def actualizar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)

    if request.method == 'POST':
        form = ClienteUpdateForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('clientes:lista_clientes')

    else:
        form = ClienteUpdateForm(instance=cliente)

    return render(request, 'clientes/actualizar_cliente.html', {'form': form, 'cliente': cliente})

# Vista para desactivar el registro de un cliente
def desactivar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    cliente.activo = False
    cliente.save()  # Guarda los cambios en la base de datos
    return redirect('clientes:listado_clientes') 


# Vista para activar el registro de un cliente
def activar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    cliente.activo = True
    cliente.save()
    return redirect('clientes:listado_clientes')
    