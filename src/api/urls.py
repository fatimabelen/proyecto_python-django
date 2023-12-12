from django.urls import path
from .views import CoordinadorListAPIView, CoordinadorRetrieveAPIVIEW

app_name = 'api'

urlpatterns = [
    path('coordinadores/', CoordinadorListAPIView.as_view(), name='listar_coordinadores'),
    path('coordinadores/<int:pk>/', CoordinadorRetrieveAPIVIEW.as_view(), name='buscar_coordinador'),
]
