from unittest.util import _MAX_LENGTH
from tabnanny import verbose
from django.db import models
from django.utils.text import slugify

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
    slug = models.SlugField(
        null=True, blank=True
    )

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return "({}): {} {}".format(self.nombre, self.precio, self.cantidad, self.fecha_ingreso, self.slug)

    def save(self, *args, **kwargs):
        if self.slug == None:
            slug = slugify(self.nombre)

            has_slug = Producto.objects.filter(slug=slug).exists()
            count = 1
            while has_slug:
                count += 1
                slug = slugify(self.nombre) + '-' + str(count) 
                has_slug = Producto.objects.filter(slug=slug).exists()

            self.slug = slug
        super().save(*args, **kwargs)