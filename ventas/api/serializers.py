from rest_framework import serializers

from inventario.models import Categoria, Producto
from ventas.models import Venta, Item


class ProductoSerializer(serializers.ModelSerializer):

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


class ItemSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer()

    class Meta:
        model = Item
        fields = ['id', 'producto', 'cantidad']


class VentaSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Venta
        fields = ['id', 'recibido', 'vuelto', 'total', 'creado', 'items']


class ItemCreateSerializer(serializers.ModelSerializer):
    producto = serializers.PrimaryKeyRelatedField(
        queryset=Producto.objects.all())

    class Meta:
        model = Item
        fields = ['producto', 'cantidad']


class VentaCreateSerializer(serializers.ModelSerializer):
    items = ItemCreateSerializer(many=True, read_only=False)

    class Meta:
        model = Venta
        fields = ['id', 'recibido', 'vuelto', 'total', 'items']

    def create(self, validated_data):
        venta = Venta.objects.create(
            recibido=validated_data.get('recibido'),
            vuelto=validated_data.get('vuelto'),
            total=validated_data.get('total'))
        items = validated_data.get('items')
        for item in items:
            Item.objects.create(venta=venta, **item)
        return validated_data


class VentasDashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = ['total', 'creado']


class ItemDashboardSerializer(serializers.ModelSerializer):
    nombre_producto = serializers.CharField()
    cantidad_vendida = serializers.IntegerField()

    class Meta:
        model = Item
        fields = ['nombre_producto', 'cantidad_vendida']


# pylint:disable=abstract-method
class DashboardSerializer(serializers.Serializer):
    ventas = VentasDashboardSerializer(many=True)
    items = ItemDashboardSerializer(many=True)
