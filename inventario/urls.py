from django.urls import path
from . import views

app_name = 'inventario'

urlpatterns = [
    path('', views.lista, name='productos'),
    path('<int:id>', views.detalle, name='producto'),
    path('crear', views.crear, name='crear'),
    path('categoria', views.crear_categoria, name='categoria'),
    path('<int:id>/actualizar', views.actualizar, name='actualizar'),
    path('<int:id>/eliminar', views.eliminar, name='eliminar'),
]
