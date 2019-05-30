from django.db import models

from inventario.models import Producto

# Create your models here.
class Venta(models.Model):

  class Meta:
    verbose_name = "Venta"
    verbose_name_plural = "Ventas"

    def __str__(self):
      pass

class Orden(models.Model):

  class Meta:
    verbose_name = "Orden"
    verbose_name_plural = "Ordenes"

  def __str__(self):
    pass
