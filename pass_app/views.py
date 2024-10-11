from django.shortcuts import render

from django.views.generic import TemplateView, UpdateView
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ProyectoEnProceso, ProyectoTerminados
from .serializers import ProyectoEnProcesoSerializer, ProyectoTerminadosSerializer


# Create your views here.
# myapp/views.py

class ProyectoEnProcesoList(APIView):
    def get(self, request):
        proyectos = ProyectoEnProceso.objects.all()
        serializer = ProyectoEnProcesoSerializer(proyectos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductoListView(ListAPIView):
    queryset = ProyectoTerminados.objects.all()  # Obtiene todas las instancias de Producto
    serializer_class = ProyectoTerminadosSerializer


class ProyectoTerminadosList(UpdateView):
    pass
