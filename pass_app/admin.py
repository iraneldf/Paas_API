from django.contrib import admin
from .models import ProyectoTerminados, ProyectoEnProceso


# Register your models here.
@admin.register(ProyectoEnProceso)
class ProyectoEnProcesoAdmin(admin.ModelAdmin):
    # resource_class = BookResource
    fieldsets = (
        ("general", {"fields": ("nombre", "imagen_principal", "anno")}),
        ("other", {"fields": ("descripcion", "iconos")}),
    )
    list_filter = ("nombre",)

    # Render filtered options only after 5 characters were entered
    # filter_input_length = {
    #     "nombre": 3,
    # }

@admin.register(ProyectoTerminados)
class ProyectoTerminadosAdmin(admin.ModelAdmin):
    # resource_class = BookResource
    fieldsets = (
        ("general", {"fields": ("nombre", "imagen_principal", "anno", "anno2")}),
        ("other", {"fields": ("descripcion", "iconos")}),
    )
    list_filter = ("nombre",)

    # Render filtered options only after 5 characters were entered
    # filter_input_length = {
    #     "nombre": 3,
    # }
