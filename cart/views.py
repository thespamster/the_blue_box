from django.shortcuts import render
from products.models import Product
import random

# Create your views here.

def view_cart(request):
    ''' Render the shopping cart page '''

    return render(request, 'cart/cart.html')