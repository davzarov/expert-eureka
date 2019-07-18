from django.contrib import admin
from .models import Categoria, Producto
from .actions import exportar_csv


class CategoriaAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'descripcion',
        'margen',
        'creado',
        'modificado')
    actions = [exportar_csv]

    class Meta:
        model = Categoria


class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'categoria',
        'imagen',
        'descripcion',
        'precio_costo',
        'precio_venta',
        'cantidad',
        'monto_total_stock',
        'disponible',
        'creado',
        'modificado')
    actions = [exportar_csv]

    class Meta:
        model = Producto


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
