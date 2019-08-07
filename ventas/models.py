from django.db import models
from django.db.models import F, Sum
from django.db.models.functions import Coalesce

from inventario.models import Producto


class Venta(models.Model):
    recibido = models.IntegerField('recibido', default=0)
    vuelto = models.IntegerField('vuelto', default=0, blank=True)
    total = models.IntegerField('total', default=0)
    creado = models.DateTimeField('creado', auto_now_add=True)
    modificado = models.DateTimeField('modificado', auto_now=True)

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'

    def __str__(self):
        return f"{self.id}-{self.creado.strftime('%d%m%Y-%H%M%S')}"

    def calcular_total(self):
        return self.items \
            .aggregate(total=Coalesce(Sum(
                F('producto__precio_venta') * F('cantidad'),
                output_field=models.IntegerField()), 0))['total']

    # pylint: disable=arguments-differ
    # def save(self, *args, **kwargs):
    #     self.total = self.calcular_total()
    #     super(Venta, self).save(*args, **kwargs)


class Item(models.Model):
    venta = models.ForeignKey(
        Venta, related_name='items', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField('cantidad', default=1)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
        unique_together = ('venta', 'producto')

    def __str__(self):
        return f"{self.id}-{self.producto}"
