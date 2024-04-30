from products.models import Category
from home.models import Doctors
from django.conf import settings



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