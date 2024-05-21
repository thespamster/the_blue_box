'''
    Context processors allowing access to certain variables
    across all of this sites apps
'''

from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Category, Product
from home.models import Doctors

def add_variable_to_context(request):
    ''' returns categories and doctors across the site '''
    categories = Category.objects.all()
    doctors = Doctors.objects.all()
    return {
        'categories': categories,
        'doctors': doctors,
    }

def cart_contents(request):
    '''
        Returns the cart contents and calculates the total cost
        and cost incl. delivery
    '''
    cart_items = []
    total_cost = 0
    product_count = 0
    cart = request.session.get('cart', {})
    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        total_cost += quantity * product.price
        product_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })
    if total_cost < settings.FREE_DELIVERY:
        delivery = settings.STANDARD_DELIVERY_COST
    else:
        delivery = 0
    total_with_delivery=Decimal(total_cost)+Decimal(delivery)
    context={
        'cart_items': cart_items,
        'total_cost': total_cost,
        'product_count': product_count,
        'standard_delivery': settings.STANDARD_DELIVERY_COST,
        'free_delivery': settings.FREE_DELIVERY,
        'delivery': delivery,
        'total_with_delivery': total_with_delivery,
    }
    return context
