from django.shortcuts import render, redirect
from .models import productos_db
from .forms import ProductoForm


def product_list(request):
    context = {
        'productos': productos_db
    }

    return render(request, 'inventory/product_list.html', context)


def product_create(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)

        if form.is_valid():
            nuevo_id = max(
                producto['id'] for producto in productos_db
            ) + 1 if productos_db else 1

            nuevo_producto = {
                'id': nuevo_id,
                'nombre': form.cleaned_data['nombre'],
                'categoria': form.cleaned_data['categoria'],
                'precio': form.cleaned_data['precio'],
                'stock': form.cleaned_data['stock'],
            }

            productos_db.append(nuevo_producto)

            return redirect('inventory:product_list')

    else:
        form = ProductoForm()

    context = {
        'form': form
    }

    return render(
        request,
        'inventory/product_form.html',
        context
    )