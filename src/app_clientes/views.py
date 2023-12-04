from django.shortcuts import render, get_object_or_404
from .models import Cliente


# Create your views here.
def listado_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})


# Vista para desactivar el registro de un cliente
def desactivar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    cliente.activo = False
    cliente.save()  # Guarda los cambios en la base de datos
    mensaje = f'El registro del cliente se desactivó con éxito'
    # falta el return
