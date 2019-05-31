from django.db import models

from inventario.models import Producto

# Create your models here.
class Venta(models.Model):
  descuento = models.Decimal('descuento', default=0, blank=True)
  creado = models.DatetimeField('creado', auto_add_now=True)
  modificado = models.DateTimeField('modificado', auto_now=True)

  class Meta:
    verbose_name = "Venta"
    verbose_name_plural = "Ventas"

  def __str__(self):
    pass

  def monto_total(self):
    pass


class Orden(models.Model):
  producto = models.ForeignKey(Producto)

  class Meta:
    verbose_name = "Orden"
    verbose_name_plural = "Ordenes"

  def __str__(self):
    pass
