from products.models import Category, Product
from home.models import Doctors
from django.conf import settings
from django.shortcuts import get_object_or_404

def add_variable_to_context(request):

    categories = Category.objects.all()
    doctors = Doctors.objects.all()

    return {
        'categories': categories,
        'doctors': doctors,
    }

def cart_contents(request):

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
        total_cost=total_cost+delivery

    context={
        'cart_items': cart_items,
        'total_cost': total_cost,
        'product_count': product_count,
        'free_delivery': settings.FREE_DELIVERY,
    }

    return context