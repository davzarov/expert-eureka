from rest_framework import viewsets

from inventario.models import Categoria
from .serializers import CategoriaSerializer


class CategoriaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
