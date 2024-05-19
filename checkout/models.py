'''
    This file contains the models for the checkout app. 
    The Order model is used to store the order details.
    The OrderLineItem model is used to store the line items of the order.
'''

import uuid
from decimal import Decimal
from django.db import models
from django.db.models import Sum
from django.conf import settings
from products.models import Product

from profiles.models import UserProfile

# Create your models here.
class Order(models.Model):
    ''' Model to store order details '''
    order_ref = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=254, null=False, blank=False)
    email = models.EmailField(max_length=254, null=True, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=False, blank=False, default='')
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    original_cart = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    def _generate_order_number(self):
        ''' generate a random 32char unique order_reference '''
        return uuid.uuid4().hex.upper()

    def update_total(self):
        ''' update grand total each time a line item is added, accounting for delivery costs '''
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        if self.order_total < settings.FREE_DELIVERY:
            self.delivery_cost = 2.99
        else:
            self.delivery_cost = 0
        self.grand_total = Decimal(self.order_total) + Decimal(self.delivery_cost)
        self.save()

    def save(self, *args, **kwargs):
        ''' 
        override the original save method to
        set the order number if it hasn't been set already
        '''
        if not self.order_ref:
            self.order_ref = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_ref

class OrderLineItem(models.Model):
    ''' Model to store line items of an order '''
    order = models.ForeignKey(Order, null=False, blank=False,
                                on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2,
                                            null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        '''
            override the original save method to set 
            the order number if it hasn't been set already
        '''
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'EAN {self.product.ean} on order {self.order.order_ref}'