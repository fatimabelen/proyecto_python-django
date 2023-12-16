from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from app_coordinadores.models import Coordinador
from app_clientes.models import Cliente
from app_servicios.models import Servicio
from app_empleados.models import Empleado
from app_reservas.models import ReservaServicio
from .serializers import ClienteSerializerList, ClienteSerializerRetrieve
from .serializers import CoordinadorSerializerList, CoordinadorSerializerRetrieve
from .serializers import ServicioSerializerList, ServicioSerializerRetrieve
from .serializers import EmpleadoSerializerList, EmpleadoSerializerRetrieve
from .serializers import ReservaSerializerList, ReservaSerializerRetrieve


# Create your views here.

# Vistas para COORDINADOR
class CoordinadorListAPIView(generics.ListAPIView):
    queryset = Coordinador.objects.all()
    serializer_class = CoordinadorSerializerList
    permission_clases = [IsAuthenticatedOrReadOnly]
        
class CoordinadorRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Coordinador.objects.all()
    serializer_class = CoordinadorSerializerRetrieve
    permission_classes = [IsAuthenticatedOrReadOnly]    

# Vistas para CLIENTE
class ClienteListAPIView(generics.ListAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializerList
    permission_classes = [IsAuthenticatedOrReadOnly]


class ClienteRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializerRetrieve
    permission_classes = [IsAuthenticatedOrReadOnly]


# Vistas para SERVICIOS
class ServicioListAPIView(generics.ListAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializerList
    permission_classes = [IsAuthenticatedOrReadOnly]

class ServicioRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializerRetrieve
    permission_classes = [IsAuthenticatedOrReadOnly]    

# Vistas para EMPLEADO
class EmpleadoListAPIView(generics.ListAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializerList
    permission_clases = [IsAuthenticatedOrReadOnly]
        
class EmpleadoRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializerRetrieve
    permission_classes = [IsAuthenticatedOrReadOnly]   

# Vistas para RESERVAS
class ReservaListAPIView(generics.ListAPIView):
    queryset = ReservaServicio.objects.all()
    serializer_class = ReservaSerializerList
    permission_clases = [IsAuthenticatedOrReadOnly]
        
class ReservaRetrieveAPIView(generics.RetrieveAPIView):
    queryset = ReservaServicio.objects.all()
    serializer_class = ReservaSerializerRetrieve
    permission_classes = [IsAuthenticatedOrReadOnly]   


def api_documentation(request):
    # Aquí puedes proporcionar la información sobre los endpoints de tu API
    return render(request, 'homepages/homepage_apis.html') 