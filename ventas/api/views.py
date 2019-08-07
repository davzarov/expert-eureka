from rest_framework import viewsets
# from rest_framework.parsers import JSONParser

from inventario.models import Categoria
from ventas.models import Venta

from .serializers import CategoriaSerializer, VentaSerializer


class CategoriaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
    # parser_classes = [JSONParser]
