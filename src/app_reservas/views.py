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
# Vista para listar reservas de servicios
class ReservasListView(generic.ListView):
    model = ReservaServicio
    fields = ['__all__']
    template_name = 'reservas/lista_reservas.html'
    context_object_name = 'reservas'


# Vista para crear nuevas reservas de servicios
class ReservasCreateView(generic.CreateView):
    model = ReservaServicio
    fields = '__all__'
    template_name = 'reservas/nueva_reserva.html'
    extra_context = {'titulo':'REGISTRAR RESERVA', 'mensaje_boton':'REGISTRAR RESERVA'}
    success_url = reverse_lazy('app_reservas:listado_reservas')

# Vista para modificar una reserva
class ReservasUpdateView(generic.UpdateView):
    model = ReservaServicio
    fields = '__all__'
    exclude = 'fecha_reserva'
    template_name = 'reservas/actualizar_reserva.html'
    success_url = reverse_lazy('app_reservas:listado_reservas')

    def form_valid(self, form):
        # Validar que el cliente/servicio/empleado/responsable esté activo
        cliente = form.cleaned_data.get('cliente') 
        servicio = form.cleaned_data.get('servicio') 
        empleado = form.cleaned_data.get('empleado') 
        coordinador = form.cleaned_data.get('coordinador')  

        if not cliente.activo or not servicio.activo or not empleado.activo or not coordinador.activo:
            form.add_error(None, 'No se puede seleccionar un elemento inactivo.')
            return self.form_invalid(form)

        return super().form_valid(form)


# Vista para eliminar una reserva de servicio
class ReservaServicioDeleteView(generic.DeleteView):
    model = ReservaServicio
    template_name = 'reservas/eliminar_reserva.html'
    extra_context = {'titulo': 'Eliminar Reserva de Servicio',
                     'mensaje_boton': 'ELIMINAR'}
    success_url = reverse_lazy('app_reservas:listado_reservas')