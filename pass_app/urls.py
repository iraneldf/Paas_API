"use client"

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import ProyectoEnProcesoViewSetCustom, MyViewSet, MiembroViewSet
from .views import ProductoListView

# Crear una instancia del router
router = DefaultRouter()

# Registrar el ViewSet con un prefijo
router.register(r'proyectos_en_curso', ProyectoEnProcesoViewSetCustom, basename='proyectos_en_curso')
# router.register(r'proyectos_en_curso2', ProyectoEnProcesoViewSet, basename='proyectos_en_curso2')
router.register(r'custom_action', MyViewSet, basename='custom_action')
router.register(r'miembros', MiembroViewSet, basename='miembros')

# Incluir las URLs del router en urlpatterns
urlpatterns = [
    path('', include(router.urls)),
    path('proyectos_en_curso_list/', ProductoListView.as_view(), name='proyectos_en_curso_list'),
]
