from django.shortcuts import render, get_object_or_404
from .models import Product


def all_products(request):
    # Shows all products

    store_products = Product.objects.all()

    context = {
        'store_products': store_products
    }
    return render(request, 'products/products.html', context)


def product_info(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_info.html', context)
