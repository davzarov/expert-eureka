from django.db import models
from django.urls import reverse


class Categoria(models.Model):
    nombre = models.CharField('nombre', max_length=255)
    descripcion = models.TextField('descripción', blank=True)
    margen = models.PositiveIntegerField('margen de venta',)
    creado = models.DateTimeField('creado', auto_now_add=True)
    modificado = models.DateTimeField('modificado', auto_now=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre

    @property
    def get_productos(self):
        return Producto.objects.filter(categoria__nombre=self.nombre)


class Producto(models.Model):
    nombre = models.CharField('nombre', max_length=255)
    categoria = models.ForeignKey(
        Categoria, related_name='productos', on_delete=models.CASCADE, blank=True, null=True)
    imagen = models.ImageField(
        'imágen', upload_to='productos/%Y/%m/%d', blank=True)
    descripcion = models.TextField('descripción', blank=True)
    precio_costo = models.IntegerField('precio de costo', default=0)
    cantidad = models.PositiveIntegerField('cantidad', default=0)
    disponible = models.BooleanField('disponible', default=True)
    creado = models.DateTimeField('creado', auto_now_add=True)
    modificado = models.DateTimeField('modificado', auto_now=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('inventario:producto', args=[self.id])

    @property
    def precio_venta(self):
        if self.categoria:
            return int(self.precio_costo + (self.precio_costo * (self.categoria.margen / 100.0)))

    @property
    def monto_total_stock(self):
        return self.precio_costo * self.cantidad
