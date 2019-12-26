from django.contrib import admin

from .models import Venta, Item

class ItemInline(admin.TabularInline):
    model = Item
    readonly_fields = ('producto', 'cantidad')
    can_delete = False
    extra = 0
    max_num = 0

class VentaAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'recibido',
        'vuelto',
        'total',
        'creado',
        'modificado')
    readonly_fields = (
        'recibido',
        'vuelto',
        'total')
    inlines = [ItemInline,]

    class Meta:
        model = Venta

admin.site.register(Venta, VentaAdmin)
