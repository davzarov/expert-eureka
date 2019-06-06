from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404

from .models import Producto
from .forms import ProductoForm

# Create your views here.
@login_required
def lista(request):
    productos = Producto.objects.order_by('-creado')
    return render(request, 'inventario/productos.html', {'productos': productos})


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
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.save()
            messages.success(request, 'Producto añadido con éxito')
            return redirect(producto.get_absolute_url())
        messages.error(request, "Algo salió mal")
    # GET
    form = ProductoForm()
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
            messages.success(request, f'Producto {producto.id} modificado con éxito')
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
        messages.success(request, f'Producto {producto_id} eliminado con éxito')
        return redirect('inventario:productos')
    return render(request, 'confirmar_eliminar.html', {'objeto': producto})
