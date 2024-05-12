from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm

# Create your views here.
def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your shopping cart at the moment")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51PFafQC0Oe68BG8jyigLuidI0hWmrsTpDzQsyPmUnsqOEYTJ5INJryAgHQlXL6r9C6xE2DvCeswoAbi9jlkqREqB0013ST5RBL',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
