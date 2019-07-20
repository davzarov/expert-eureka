from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# from django.shortcuts import render
from inventario.models import Categoria


@login_required
def categorias_json(request):
    categorias = list(Categoria.objects.order_by('nombre').values())
    return JsonResponse(categorias, safe=False)
