from django.shortcuts import render, get_object_or_404
from products.models import Product
import random

# Create your views here.

def index(request):
    ''' Render the home page '''

    ''' get 6 random products for a featured section on the home page '''

    products = Product.objects.all()
    quantity = Product.objects.count()
    start = random.randint(0, (quantity-6))
    image1 = get_object_or_404(Product, pk=start).image_url
    image2 = get_object_or_404(Product, pk=start+1).image_url
    image3 = get_object_or_404(Product, pk=start+2).image_url
    image4 = get_object_or_404(Product, pk=start+3).image_url
    image5 = get_object_or_404(Product, pk=start+4).image_url
    image6 = get_object_or_404(Product, pk=start+5).image_url

    context = {
        'products': products,
        'start_pos': start,
        'image1': image1,
        'image2': image2,
        'image3': image3,
        'image4': image4,
        'image5': image5,
        'image6': image6,
    }

    return render(request, 'home/index.html', context)
