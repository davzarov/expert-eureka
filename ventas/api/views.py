from rest_framework import viewsets
from rest_framework.decorators import action

from inventario.models import Categoria
from .serializers import CategoriaSerializer


# @action(detail=True, methods=['get'])
class CategoriaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
