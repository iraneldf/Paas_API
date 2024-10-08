# Generated by Django 4.2.16 on 2024-10-02 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Icono',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='imagenes/iconos/')),
            ],
        ),
        migrations.CreateModel(
            name='Poyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Ingrese el título completo del proyecto.', max_length=100)),
                ('descripcion', models.TextField()),
                ('imagen_principal', models.ImageField(upload_to='imagenes/proyectos/')),
                ('iconos', models.ManyToManyField(blank=True, to='pass_app.icono')),
            ],
        ),
        migrations.CreateModel(
            name='ProyectoEnProceso',
            fields=[
                ('poyecto_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pass_app.poyecto')),
                ('anno', models.PositiveIntegerField(default='2024', verbose_name='año de inicio')),
            ],
            bases=('pass_app.poyecto',),
        ),
        migrations.CreateModel(
            name='ProyectoTerminados',
            fields=[
                ('poyecto_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pass_app.poyecto')),
                ('anno', models.PositiveIntegerField(default='2024', verbose_name='año de inicio')),
                ('anno2', models.PositiveIntegerField(default='2024', verbose_name='año de cierre')),
            ],
            bases=('pass_app.poyecto',),
        ),
    ]
