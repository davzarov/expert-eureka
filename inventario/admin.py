from django.contrib import admin
from .models import Producto

# Register your models here.
admin.site.site_header = "Punto de Ventas"
admin.site.register(Producto)
