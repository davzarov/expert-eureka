from rest_framework import routers

from .views import CategoriaViewSet


router = routers.DefaultRouter()
router.register(r'categorias', CategoriaViewSet)