from rest_framework.serializers import (
    ModelSerializer,
    PrimaryKeyRelatedField
)

from inventario.models import Categoria, Producto
from ventas.models import Venta, Item


class ProductoSerializer(ModelSerializer):

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


class CategoriaSerializer(ModelSerializer):
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


class ItemSerializer(ModelSerializer):
    producto = PrimaryKeyRelatedField(queryset=Producto.objects.all())
    # producto = ProductoSerializer()

    class Meta:
        model = Item
        fields = ['id', 'producto', 'cantidad']


class VentaSerializer(ModelSerializer):
    items = ItemSerializer(many=True, read_only=False)

    class Meta:
        model = Venta
        fields = ['id', 'recibido', 'vuelto', 'total', 'items']

    def create(self, validated_data):
        venta = Venta.objects.create(
            recibido=validated_data.get('recibido'),
            vuelto=validated_data.get('vuelto'))
        items = validated_data.get('items')
        for item in items:
            Item.objects.create(
                venta=venta,
                **item
            )
        return validated_data
