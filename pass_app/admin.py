from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from solo.admin import SingletonModelAdmin

from .models import ProyectoTerminados, ProyectoEnProceso, Icono, Miembro, Contactenos


# Register your models here.

class IconoInline(admin.TabularInline):  # O usa StackedInline si prefieres
    model = Icono  # Usa la tabla intermedia
    extra = 1  # Número de formularios vacíos a mostrar


@admin.register(ProyectoEnProceso)
class ProyectoEnProcesoAdmin(admin.ModelAdmin):
    list_filter = ("nombre",)
    inlines = [IconoInline]  # Añade el Inline aquí
    list_display = ('nombre', 'anno', 'delete_button')

    def delete_button(self, obj):
        url = reverse('admin:pass_app_proyectoterminados_delete', args=[obj.id])
        return format_html('<a class="button" href="{}">Eliminar</a>', url)

    delete_button.allow_tags = True  # Permitir HTML
    delete_button.short_description = 'Delete'  # Título del campo


@admin.register(ProyectoTerminados)
class ProyectoTerminadosAdmin(admin.ModelAdmin):
    list_filter = ("nombre",)
    inlines = [IconoInline]  # Añade el Inline aquí

    # Render filtered options only after 5 characters were entered
    # filter_input_length = {
    #     "nombre": 3,
    # }
    # resource_class = BookResource
    # fieldsets = (
    #     ("general", {"fields": ("nombre", "imagen_principal", "anno", "anno2")}),
    #     ("other", {"fields": ("descripcion", "iconos")}),
    # )


@admin.register(Miembro)
class MiembroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cargo')


@admin.register(Contactenos)
class ContactenosAdmin(SingletonModelAdmin):
    model = Contactenos
