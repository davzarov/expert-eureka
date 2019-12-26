from collections import namedtuple

from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.response import Response

from inventario.models import Categoria
from ventas.models import (
    Venta,
    Item
)

from .serializers import (
    CategoriaSerializer,
    DashboardSerializer,
    VentaSerializer,
    VentaCreateSerializer,
)

Dashboard = namedtuple('Dashboard', ('ventas', 'items'))


class CategoriaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class DashboardViewset(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    # pylint:disable=no-self-use
    def list(self, request):
        dashboard = Dashboard(
            ventas=Venta.objects.all(),
            items=Item.objects.best_sellers()
        )
        serializer = DashboardSerializer(dashboard)
        return Response(serializer.data)


class VentaViewset(viewsets.ModelViewSet):
    queryset = Venta.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return VentaSerializer
        if self.action == 'create':
            return VentaCreateSerializer
