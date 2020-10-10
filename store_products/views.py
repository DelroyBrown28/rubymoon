from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category


def all_products(request):
    # Shows all products

    store_products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                store_products = store_products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            store_products = store_products.order_by(sortkey)



        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            store_products = store_products.filter(
                category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        """ Search functionality"""
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter a search query")
                return redirect(reverse('store_products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            store_products = store_products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'store_products': store_products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting' : store_products,

    }
    return render(request, 'products/products.html', context)


def product_info(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_info.html', context)
