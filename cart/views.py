from django.shortcuts import render, redirect, get_object_or_404, reverse
from store_products.models import Product


def view_cart(request):
    # Bag contents
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """Adds a certain amount to the cart"""
    amount = int(request.POST.get('amount'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    cart = request.session.get('cart', {})

    if size:
        if item_id in list(cart.keys()):
            if size in cart[item_id]['items_by_size'].keys():
                cart[item_id]['items_by_size'][size] += amount
            else:
                cart[item_id]['items_by_size'][size] = amount
        else:
            cart[item_id] = {'items_by_size': {size: amount}}
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += amount
        else:
            cart[item_id] = amount

    request.session['cart'] = cart
    return redirect(redirect_url)


def edit_cart(request, item_id):
    """Edit amount of its in the cart"""

    product = get_object_or_404(Product, pk=item_id)
    amount = int(request.POST.get('amount'))
    size = None
    if 'item_has_size' in request.POST:
        size = request.POST['item_size']
    cart = request.session.get('cart', {})

    if size:
        if amount > 0:
            cart[item_id]['items_by_size'][size] = amount
        else:
            del cart[item_id]['items_by_size'][size]
    else:
        if amount > 0:
            cart[item_id] = amount
        else:
            cart.pop[item_id]

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
