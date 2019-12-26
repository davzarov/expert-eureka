from django.db import models
from django.db.models import Sum, F

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


class ItemQuerySet(models.QuerySet):
    def best_sellers(self):
        return self.annotate(nombre_producto=F('producto__nombre')).values('nombre_producto') \
            .annotate(cantidad_vendida=Sum(F('cantidad') * F('producto__precio_venta'))) \
                .order_by('-cantidad_vendida')[:5]


class ItemManager(models.Manager):
    def get_queryset(self):
        return ItemQuerySet(self.model, using=self._db)

    def best_sellers(self):
        return self.get_queryset().best_sellers()


class Item(models.Model):
    venta = models.ForeignKey(
        Venta, related_name='items', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField('cantidad', default=1)

    objects = ItemManager()

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
        unique_together = ('venta', 'producto')

    def __str__(self):
        return f"{self.producto}"
