from unittest.util import _MAX_LENGTH
from tabnanny import verbose
from django.db import models


# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(
        null=False,
        blank=False,
        max_length = 64
    )
    precio = models.FloatField(
        null=False,
        blank=False
    )
    cantidad= models.IntegerField(
        null=False,
         blank=False
    )
    fecha_ingreso= models.DateField(
        null=False,
        blank=False
    )
   
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return "({}): {} {}".format(self.nombre, self.precio, self.cantidad, self.fecha_ingreso)

