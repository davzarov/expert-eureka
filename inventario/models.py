from django.db import models
from django.urls import reverse

# Create your models here.
class Producto(models.Model):
  nombre = models.CharField('nombre', max_length=255)
  imagen = models.ImageField('imágen', upload_to='productos/%Y/%m/%d', blank=True)
  descripcion = models.TextField('descripción', blank=True)
  precio = models.IntegerField('precio',)
  stock = models.PositiveIntegerField('stock',)
  disponible = models.BooleanField('disponible', default=True)
  creado = models.DateTimeField('creado', auto_now_add=True)
  modificado = models.DateTimeField('modificado', auto_now=True)

  class Meta:
    verbose_name = "Producto"
    verbose_name_plural = "Productos"

  def __str__(self):
    return self.nombre

  def get_absolute_url(self):
    # return reverse('inventario:producto', args=[self.id])
    pass
