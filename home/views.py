from django.shortcuts import render, get_object_or_404
from products.models import Product
import random

# Create your views here.

def index(request):
    ''' Render the home page '''

    ''' get 6 random products for a featured section on the home page '''

    products = Product.objects.all()
    quantity = Product.objects.count()
    start = random.randint(0, (quantity-2))
    featured_products = products[slice(start, start+2)]

    context = {
        'products': products,
        'featured_products': featured_products,
    }

    return render(request, 'home/index.html', context)
