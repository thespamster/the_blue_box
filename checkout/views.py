'''
    Methods for checkout views
'''

import json
from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
import stripe
from products.models import Product
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from blue_box_exchange.context_processors import cart_contents
from .models import OrderLineItem
from .forms import Order, OrderForm

# Create your views here.
@require_POST
def cache_checkout_data(request):
    ''' Cache the checkout data '''
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)
def checkout(request):
    ''' Handle the checkout process '''
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'town_or_city': request.POST['town_or_city'],
            'county': request.POST['county'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart)
            order.save()
            for item_id, item_data in cart.items():
                try:
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=item_data,
                    )
                    order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your shopping cart wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_cart'))
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_ref]))
        else:
            messages.error(request, 'There was an error with your form. Please double check your information.')
    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "There's nothing in your shopping cart at the moment")
            return redirect(reverse('products'))
        current_cart = cart_contents(request)
        total_cost = current_cart['total_with_delivery']
        stripe_total = round(total_cost * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                # Attach the user's profile to the order
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

        messages.info(request, 'Once the order is submitted please wait for confirmation. Do not close/refresh the page.')
        client_secret= intent.client_secret
        template = 'checkout/checkout.html'
        context = {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': client_secret,
        }
    return render(request, template, context)

def checkout_success(request, order_ref):
    ''' Handle successful checkouts '''
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_ref=order_ref)
    order_items = OrderLineItem.objects.filter(order=order.id)
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()
    # Save the user's info
    if save_info:
        profile_data = {
            'default_phone_number': order.phone_number,
            'default_country': order.country,
            'default_postcode': order.postcode,
            'default_town_or_city': order.town_or_city,
            'default_street_address1': order.street_address1,
            'default_street_address2': order.street_address2,
            'default_county': order.county,
        }
        user_profile_form = UserProfileForm(profile_data, instance=profile)
        if user_profile_form.is_valid():
            user_profile_form.save()
    messages.success(request, f'Order successfully processed! Your order number is {order_ref}. A confirmation email will be sent to {order.email}.')
    # Send the user a confirmation email
    cust_email = order.email
    subject = render_to_string(
        'confirmation_emails/confirmation_email_subject.txt',
        {'order': order}
    )
    body = render_to_string(
        'confirmation_emails/confirmation_email_body.txt',
        {'bbs_email': settings.DEFAULT_FROM_EMAIL,
        'order': order}
    )
    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [cust_email]
    )
    if 'cart' in request.session:
        del request.session['cart']
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'order_items': order_items,
    }
    return render(request, template, context)
