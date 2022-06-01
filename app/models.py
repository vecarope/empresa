from django.db import models
import datetime


opciones_servicios= [
    [0 ,'Internet'],
    [1 , 'Telefonía Movil'],
    [2 , 'Telefonia Fija'],
]

opciones_consulta=[
    [0 ,'cotizacion'],
    [1 , 'Reclamo'],
    [2 , 'Contratación'],
]
# Create your models here.
class Solicitud(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=15)
    apellido_usuario = models.CharField(max_length=15)
    rut= models.IntegerField()
    email= models.EmailField()
    numero_telefono= models.IntegerField()
    fecha = models.DateField(default=datetime.date.today)
    servicio = models.IntegerField(choices= opciones_servicios)
    tipo_consulta = models.IntegerField(choices=opciones_consulta)
    descripcion = models.TextField(max_length=200)
    
    def __str__(self):
        return self.rut
    