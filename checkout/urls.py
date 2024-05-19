'''
    This file is used to create the urls for the checkout app.
'''

from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_ref>', views.checkout_success, name='checkout_success'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
    path('wh/', webhook, name='webhook'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
