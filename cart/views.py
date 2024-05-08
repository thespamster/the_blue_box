from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from products.models import Product

# Create your views here.

def view_cart(request):
    ''' Render the shopping cart page '''

    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    messages.success(request, f'Added  {product.name} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)

def update_cart(request, item_id):
    ''' Update the quantity or delete item from cart if quantity is 0 '''

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if quantity == 0:
        if item_id in list(cart.keys()):
            del request.session['cart'][item_id]
            messages.warning(request, f'Item {product.name} removed from your cart')
    else:
        cart[item_id] = quantity
        messages.success(request, f'Updated quantity of {product.name} in your cart')
        


    request.session['cart'] = cart
    return redirect(redirect_url)