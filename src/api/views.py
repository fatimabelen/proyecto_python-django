from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from app_coordinadores.models import Coordinador
from app_clientes.models import Cliente
from .serializers import CoordinadorSerializer, ClienteSerializer


# Create your views here.

# Vistas para COORDINADOR
class CoordinadorListAPIView(generics.ListAPIView):
    queryset = Coordinador.objects.all()
    serializer_class = CoordinadorSerializer
    permission_clases = [IsAuthenticatedOrReadOnly]

        
class CoordinadorRetrieveAPIVIEW(generics.RetrieveAPIView):
    queryset = Coordinador.objects.all()
    serializer_class = CoordinadorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]    

# Vistas para CLIENTE
class ClienteListAPIView(generics.ListAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ClienteRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]