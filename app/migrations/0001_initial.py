# Generated by Django 4.0.4 on 2022-05-31 21:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('nombre_usuario', models.CharField(max_length=15)),
                ('apellido_usuario', models.CharField(max_length=15)),
                ('rut', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('direccion', models.CharField(max_length=30)),
                ('numero_telefono', models.IntegerField(max_length=9)),
                ('fecha', models.DateField(default=datetime.date.today)),
                ('servicio', models.IntegerField(choices=[[0, 'Internet'], [1, 'Telefonía Movil'], [2, 'Telefonia Fija']])),
                ('tipo_consulta', models.IntegerField(choices=[[0, 'cotizacion'], [1, 'Reclamo'], [2, 'Contratación']])),
                ('descripcion', models.TextField(max_length=200)),
            ],
        ),
    ]