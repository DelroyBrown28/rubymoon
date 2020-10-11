from django.shortcuts import render


def view_cart(request):
    # Bag contents
    return render(request, 'cart/cart.html')