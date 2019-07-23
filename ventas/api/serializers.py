from rest_framework import serializers
from inventario.models import Categoria, Producto


class ProductoSerializer(serializers.ModelSerializer):
    precio_venta = serializers.IntegerField(read_only=True)

    class Meta:
        model = Producto
        fields = [
            'id',
            'nombre',
            'imagen',
            'precio_venta',
            'cantidad',
            'disponible'
        ]


class CategoriaSerializer(serializers.ModelSerializer):
    productos = ProductoSerializer(many=True, read_only=True)

    class Meta:
        model = Categoria
        fields = [
            'id',
            'nombre',
            'productos',
            'descripcion',
            'margen'
        ]
