from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404

from .models import Producto, Categoria
from .forms import ProductoForm, CategoriaForm


@login_required
def lista(request):
    categorias = Categoria.objects.order_by('nombre')
    return render(request, 'inventario/productos.html', {
        'categorias': categorias})


@login_required
def detalle(request, id):
    try:
        producto = Producto.objects.get(id=id)
    except Producto.DoesNotExist:
        raise Http404("El Producto que solicitó no existe.")
    return render(request, 'inventario/producto.html', {'producto': producto})


@login_required
def crear(request):
    # POST
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.save()
            messages.success(request, 'Producto añadido con éxito')
            return redirect(producto.get_absolute_url())
        messages.error(request, 'Algo salió mal')
    # GET
    form = ProductoForm()
    return render(request, 'inventario/crear.html', {'form': form})


@login_required
def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            categoria = form.save(commit=False)
            categoria.save()
            messages.success(request, 'Categoría añadida con éxito')
            return redirect('inventario:productos')
        messages.error(request, 'Algo salió mal')
    form = CategoriaForm()
    return render(request, 'inventario/crear.html', {'form': form})


@login_required
def actualizar(request, id):
    producto = get_object_or_404(Producto, id=id)
    # POST
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.save()
            messages.success(
                request, f'Producto {producto.id} modificado con éxito')
            return redirect(producto.get_absolute_url())
        messages.error(request, "Algo salió mal")
    form = ProductoForm(instance=producto)
    return render(request, 'inventario/crear.html', {'form': form})


@login_required
def eliminar(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto_id = producto.id
    # POST
    if request.method == 'POST':
        producto.delete()
        messages.success(
            request, f'Producto {producto_id} eliminado con éxito')
        return redirect('inventario:productos')
    return render(request, 'confirmar_eliminar.html', {'objeto': producto})
