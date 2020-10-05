from django.shortcuts import render
from .models import Product


def all_products(request):
    # Shows all products

    store_products = Product.objects.all()

    context = {
        'store_products': store_products
    }
    return render(request, 'products/products.html', context)
