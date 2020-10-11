from decimal import Decimal
from django.conf import settings


def cart_contents(request):

    cart_items = []
    total = 0
    product_amount = 0

    if total < settings.FREE_DELIVERY_METER:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE/100)
        free_delivery = settings.FREE_DELIVERY_METER - total
    else:
        delivery = 0
        free_delivery = 0
    
    grand_total = delivery + total

    context = {
        'cart_items' : cart_items,
        'total' : total,
        'product_amount' : product_amount,
        'delivery' : delivery,
        'free_delivery' : free_delivery,
        'free_delivery_meter' : settings.FREE_DELIVERY_METER,
        'grand_total' : grand_total,

    }
    return context
