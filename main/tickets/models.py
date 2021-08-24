from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Tickets(models.Model):
    TIPO = (
			('c', 'Creado'),
			('ep', 'En proceso'),
			('ce', 'Cerrado'),
			)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_inicio = models.DateTimeField(default=datetime.now())
    fecha_fin = models.DateTimeField(default=datetime.now())
    descripcion = models.CharField(max_length = 200)
    estado = models.CharField(blank=True, null = True, max_length=15, choices=TIPO, default='c')

    def __str__(self):
        return '{}'.format(self.usuario)