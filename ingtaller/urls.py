"""ingtaller URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from rest_framework import routers

from ventas.api.views import CategoriaViewSet, VentaViewSet

admin.site.site_header = "Administración de Punto de Ventas"

router = routers.DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'ventas', VentaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(pattern_name='dashboard:dashboard')),
    path('dashboard/', include('dashboard.urls')),
    path('inventario/', include('inventario.urls')),
    path('ventas/', include('ventas.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
