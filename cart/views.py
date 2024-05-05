from django.shortcuts import render,redirect

# Create your views here.

def view_cart(request):
    ''' Render the shopping cart page '''

    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """


    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)

def update_cart(request, item_id):
    ''' Update the quantity or delete item from cart if quantity is 0 '''

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if quantity == 0:
        if item_id in list(cart.keys()):
            del request.session['cart'][item_id]
    else:
        cart[item_id] = quantity


    request.session['cart'] = cart
    return redirect(redirect_url)