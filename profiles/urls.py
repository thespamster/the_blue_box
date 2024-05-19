'''
    This file is used to define the urls for the profiles app.
'''

from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_ref>', views.order_history, name='order_history'),
]
 