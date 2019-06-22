# from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from django.http import Http404
from django.shortcuts import render # , redirect, get_object_or_404

from inventario.models import Categoria


@login_required
def pos(request):
    categorias = Categoria.objects.order_by('nombre')
    return render(request, 'ventas/pos.html', {
        'categorias': categorias
    })
