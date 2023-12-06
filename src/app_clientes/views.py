from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.views import generic
from django.urls import reverse_lazy
from .models import Cliente
from .forms import ClienteUpdateForm

# Create your views here.

def listado_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})

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

# activar clientes
class ClienteUpdateView(generic.UpdateView):
    model = Cliente
    fields = ['activo', 'nombre', 'apellido']
    extra_context = {'titulo': 'ACTIVAR CLIENTE', 'mensaje_boton': 'GUARDAR CAMBIOS'}
    template_name = 'clientes/activar.html'
    

class ClienteCreateView(generic.CreateView): 
    model = Cliente
    fields = '__all__'
    template_name = 'clientes/nuevo.html'
    extra_context = {'titulo': 'ALTA DE CLIENTE', 'mensaje_boton': 'CREAR'}
    success_url = reverse_lazy("clientes:lista_clientes")
  