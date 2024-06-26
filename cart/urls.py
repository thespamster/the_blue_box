'''
    This file is used to define the urls for the cart app.
'''

from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views



urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add/<item_id>/', views.add_to_cart, name='add_to_cart'),
    path('update/<item_id>/', views.update_cart, name='update_cart'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)