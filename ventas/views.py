from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from inventario.models import Categoria


@login_required
def pos(request):
    categorias = Categoria.objects.order_by('nombre')
    return render(request, 'ventas/pos.html', {
        'categorias': categorias
    })
