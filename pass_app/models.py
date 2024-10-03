from django.db import models


# Create your models here.

class Poyecto(models.Model):
    nombre = models.CharField(max_length=100, help_text="Ingrese el título completo del proyecto.")
    descripcion = models.TextField()
    imagen_principal = models.ImageField(upload_to='imagenes/proyectos/')  # Ruta donde se guardarán las imágenes
    iconos = models.ManyToManyField('Icono', blank=True)  # Relación con el modelo Icono

    def __str__(self):
        return self.nombre


class ProyectoEnProceso(Poyecto):
    anno = models.PositiveIntegerField(verbose_name='año de inicio',
                                       default='2024')  # Campo para el año, solo números positivos

    def __str__(self):
        return f'{super().__str__()} - {self.anno}'


class ProyectoTerminados(Poyecto):
    anno = models.PositiveIntegerField(verbose_name='año de inicio',
                                       default='2024')  # Campo para el año, solo números positivos
    anno2 = models.PositiveIntegerField(verbose_name='año de cierre',
                                        default='2024')  # Campo para el año, solo números positivos

    def __str__(self):
        return f'{super().__str__()} - {self.anno} - {self.anno2}'


class Icono(models.Model):
    imagen = models.ImageField(upload_to='imagenes/iconos/')  # Ruta para las imágenes de iconos

    def __str__(self):
        return f'Icono {self.id}'  # Representación simple del icono
