from django.shortcuts import render, redirect


def view_cart(request):
    # Bag contents
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """Adds a certain amount to the bag"""

    amount = int(request.POST.get('amount'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += amount
    else:
        cart[item_id] = amount

    request.session['cart'] = cart
    return redirect(redirect_url)
