from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from app_coordinadores.models import Coordinador
from app_clientes.models import Cliente
from app_servicios.models import Servicio
from .serializers import ClienteSerializerList, ClienteSerializerRetrieve
from .serializers import CoordinadorSerializerList, CoordinadorSerializerRetrieve
from .serializers import ServicioSerializerList, ServicioSerializerRetrieve
# Create your views here.

# Vistas para COORDINADOR
class CoordinadorListAPIView(generics.ListAPIView):
    queryset = Coordinador.objects.all()
    serializer_class = CoordinadorSerializerList
    permission_clases = [IsAuthenticatedOrReadOnly]
        
class CoordinadorRetrieveAPIVIEW(generics.RetrieveAPIView):
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