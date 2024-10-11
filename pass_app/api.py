from django.http import HttpResponse
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet, GenericViewSet, ViewSet

from .models import ProyectoEnProceso, Miembro
from .serializers import ProyectoEnProcesoSerializer, MiembroSerializer


class ProyectoEnProcesoViewSetCustom(ReadOnlyModelViewSet):
    queryset = ProyectoEnProceso.objects.all()
    serializer_class = ProyectoEnProcesoSerializer

    # permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['get'])
    def custom_action(self, request, pk=None):
        # Lógica personalizada aquí
        return Response({'status': 'password set'})


# class ProyectoEnProcesoViewSet(mixins.ListModelMixin,
#                                mixins.CreateModelMixin,
#                                GenericViewSet):
#     queryset = ProyectoEnProceso.objects.all()
#     serializer_class = ProyectoEnProcesoSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


class MyViewSet(ViewSet):

    @action(detail=True, methods=['get'])
    def custom_action(self, request, pk=None):
        # Lógica personalizada aquí
        return Response({'status': 'password set'})


# un viewset para el modelo Miembro
class MiembroViewSet(ReadOnlyModelViewSet):
    queryset = Miembro.objects.all()
    serializer_class = MiembroSerializer
