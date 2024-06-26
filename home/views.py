'''
    This file contains the views for the home app.
'''

import random
from django.shortcuts import render
from products.models import Product


# Create your views here.

def index(request):
    ''' Render the home page '''
    products = Product.objects.all()
    quantity = Product.objects.count()
    start = random.randint(0, (quantity-2))
    featured_products = products[slice(start, start+2)]
    context = {
        'products': products,
        'featured_products': featured_products,
    }
    return render(request, 'home/index.html', context)
