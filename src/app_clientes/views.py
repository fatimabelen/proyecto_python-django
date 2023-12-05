from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Cliente


# Create your views here.
#def listado_clientes(request):
#   clientes = Cliente.objects.all()
#   return render(request, 'clientes:lista_clientes.html', {'clientes': clientes})


class ClientesListView(generic.ListView):
    model = Cliente
    fields = '__all__'
    template_name = 'clientes/lista_clientes.html'
    context_object_name = 'clientes'

    # Función para desactivar clientes
"""
    def post(self, request, *args, **kwargs):
        cliente_id = request.POST.get('cliente_id')
        cliente = Cliente.objects.get(pk=cliente_id)
        cliente.activo = False
        cliente.save()
        return self.get(request, *args, **kwargs)

"""
# Vista para desactivar el registro de un cliente
"""
def desactivar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    cliente.activo = False
    cliente.save()  # Guarda los cambios en la base de datos
    mensaje = f'El registro del cliente se desactivó con éxito'
    # falta el return
"""