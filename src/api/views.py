from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from app_coordinadores.models import Coordinador
from .serializers import CoordinadorSerializer


# Create your views here.

class CoordinadorListAPIView(generics.ListAPIView):
    queryset = Coordinador.objects.all().values('nombre', 'apellido')
    serializer_class = CoordinadorSerializer
    permission_clases = [IsAuthenticatedOrReadOnly]

        
class CoordinadorRetrieveAPIVIEW(generics.RetrieveAPIView):
    queryset = Coordinador.objects.all()
    serializer_class = CoordinadorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]    
