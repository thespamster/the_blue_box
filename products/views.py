from django.shortcuts import render,redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category

# Create your views here.

def all_products(request):
    ''' A view to show all products, including sorting and search queries '''

    products = Product.objects.all()
    categories = Category.objects.all()
    
    query = None

    if request.GET:

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
                messages.error(request, "You didn't enter any search criteria!")
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

    context = {
        'product': product,
        'tags': product.tags.split(','),
    }

    

    return render(request, 'products/product_detail.html', context)
