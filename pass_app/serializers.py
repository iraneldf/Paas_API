# myapp/serializers.py
from rest_framework import serializers
from .models import ProyectoEnProceso, ProyectoTerminados, Miembro


class ProyectoEnProcesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProyectoEnProceso
        fields = '__all__'


class ProyectoTerminadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProyectoTerminados
        fields = '__all__'


class MiembroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Miembro
        fields = '__all__'
