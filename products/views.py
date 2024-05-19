'''
    This file contains the views for the products app.
'''

from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.urls import reverse
from .models import Product, Category

# Create your views here.
def all_products(request):
    ''' A view to show all products, including sorting and search queries '''
    products = Product.objects.all().order_by('price')
    categories = Category.objects.all()
    query = None
    if request.GET:
        if 'rating' in request.GET:
            query = request.GET['rating']
            if not query:
                messages.error(request, "No rating search criteria!")
                return redirect(reverse('products'))
            queries = query.split('-')
            products = products.filter(rating__range=(int(queries[0]), int(queries[1])))
        if 'price' in request.GET:
            query = request.GET['price']
            if not query:
                messages.error(request, "No price search criteria!")
                return redirect(reverse('products'))
            queries = query.split('-')
            if queries[1] == '101':
                query = 100
                products = products.filter(price__gte=query)
            else:
                products = products.filter(price__range=(queries[0], queries[1]))
        if 'category' in request.GET:
            query = request.GET['category']
            if not query:
                messages.error(request, "No category search criteria!")
                return redirect(reverse('products'))
            queries = categories.filter(name=query)
            queries = queries[slice(0,1)]
            products = products.filter(category=queries)
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.info(request, "Add a search term and try searching again!")
                return redirect(reverse('products'))
            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(tags__icontains=query)
            products = products.filter(queries)
    context = {
        'products': products,
        'categories': categories,
        'search_term': query,
    }
    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    ''' A view to show a products info '''
    product = get_object_or_404(Product, pk=product_id)
    query = product_id
    context = {
        'product': product,
        'tags': product.tags.split(','),
        'search_term': query,
    }
    return render(request, 'products/product_detail.html', context)
