from django.db import models
from django.db.models import ForeignKey
from solo.models import SingletonModel


# Create your models here.

class Proyecto(models.Model):
    nombre = models.CharField(max_length=100, help_text="Ingrese el título completo del proyecto.")
    descripcion = models.TextField()
    imagen_principal = models.ImageField(upload_to='imagenes/proyectos/')  # Ruta donde se guardarán las imágenes

    def __str__(self):
        return self.nombre


class ProyectoEnProceso(Proyecto):
    anno = models.PositiveIntegerField(verbose_name='año de inicio',
                                       default='2024')  # Campo para el año, solo números positivos

    def __str__(self):
        return f'{super().__str__()} - {self.anno}'


class ProyectoTerminados(Proyecto):
    anno = models.PositiveIntegerField(verbose_name='año de inicio',
                                       default='2024')  # Campo para el año, solo números positivos
    anno2 = models.PositiveIntegerField(verbose_name='año de cierre',
                                        default='2024')  # Campo para el año, solo números positivos

    def __str__(self):
        return f'{super().__str__()} - {self.anno} - {self.anno2}'


class Icono(models.Model):
    imagen = models.ImageField(upload_to='imagenes/iconos/')  # Ruta para las imágenes de iconos
    proyecto = ForeignKey(Proyecto, related_name='iconos', on_delete=models.CASCADE)

    def __str__(self):
        return f'Icono {self.id}'  # Representación simple del icono


# Crear un modelo llamado Miembro
class Miembro(models.Model):
    nombre = models.CharField(max_length=200, verbose_name='nombre')
    avatar = models.ImageField(upload_to='imagenes/avatars/', null=True, blank=True)
    cargo = models.CharField(max_length=200, verbose_name='cargo')
    facebookAct = models.BooleanField(default=False, verbose_name='Facebook')
    facebook = models.URLField(unique=True, verbose_name='Link', blank=True, null=True)
    whatsappAct = models.BooleanField(default=False, verbose_name='Whatsapp')
    whatsapp = models.URLField(unique=True, verbose_name='Link', blank=True, null=True)
    twitterAct = models.BooleanField(default=False, verbose_name='Twitter')
    twitter = models.CharField(max_length=100, verbose_name='Link', default='/', blank=True)
    instagramAct = models.BooleanField(default=False, verbose_name='Instagram')
    instagram = models.CharField(max_length=100, verbose_name='Link', default='/', blank=True)
    linkedinAct = models.BooleanField(default=False, verbose_name='Linkedin')
    linkedin = models.CharField(max_length=100, verbose_name='Link', default='/', blank=True)

    def __str__(self):
        return f'{self.nombre}'


class Contactenos(SingletonModel):
    ubicacion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField()
    ubicacion_mapa = models.CharField(max_length=255)  # Puede ser una URL del mapa

    def __str__(self):
        return f"Contacto: {self.telefono}, {self.correo}"
