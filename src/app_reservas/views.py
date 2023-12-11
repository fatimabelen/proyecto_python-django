from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from .models import ReservaServicio
from app_clientes.models import Cliente
from app_coordinadores.models import Coordinador
from app_empleados.models import Empleado
from app_servicios.models import Servicio


# Create your views here.

# Vista para crear nuevas reservas de servicios
class ReservasCreateView(generic.CreateView):
    model = ReservaServicio
    fields = '__all__'
    template_name = 'reservas/formulario_reserva.html'
    extra_context = {'titulo':'REGISTRAR RESERVA', 'mensaje_boton':'REGISTRAR RESERVA'}
    #success_url = reverse_lazy('app_reservas:listado_reservas')

# Vista para editar una reserva de servicio
def editar_reserva(request, pk):
    reserva = get_object_or_404(ReservaServicio, pk=pk)
    clientes_activos = Cliente.objects.filter(activo=True)
    servicios_activos = Servicio.objects.filter(activo=True)
    empleados_activos = Empleado.objects.filter(activo=True)
    coordinadores_activos = Coordinador.objects.filter(activo=True)

    return render(request, 'reservas/actualizar_reserva.html', {
        'reserva': reserva,
        'clientes_activos': clientes_activos,
        'servicios_activos': servicios_activos,
        'empleados_activos': empleados_activos,
        'coordinadores_activos': coordinadores_activos,
    })

# Vista para eliminar una reserva de servicio
class ReservaServicioDeleteView(generic.DeleteView):
    model = ReservaServicio
    template_name = 'reservas/confirmar_eliminar_reserva.html'
    success_url = reverse_lazy('app_reservas:listado_reservas')

    def delete(self, request, *args, **kwargs):
        messages.success(request, "La reserva se eliminó correctamente.")
        return super().delete(request, *args, **kwargs)