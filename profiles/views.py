'''
    This file is used to create the views for the user profile page.
'''

from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from checkout.models import Order, OrderLineItem
from .models import UserProfile
from .forms import UserProfileForm

# Create your views here.
@login_required
def profile(request):
    ''' Display the user's profile '''
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request,
                ('Update failed. Please ensure the form is valid.'))
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
    }
    return render(request, template, context)

def order_history(request, order_ref):
    ''' Display the user's order history '''
    order = get_object_or_404(Order, order_ref=order_ref)
    order_items = OrderLineItem.objects.filter(order=order.id)
    messages.info(request, (
        f'This is a past confirmation for order number {order_ref}. '
        'A confirmation email was sent on the order date.'
    ))
    template = 'checkout/checkout_success.html'
    context = {
        'order_items': order_items,
        'order': order,
        'from_profile': True,
    }
    return render(request, template, context)
