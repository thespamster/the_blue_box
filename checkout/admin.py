'''
    This file is used to register the Order and OrderLineItem models with the Django admin site.
'''

from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.
class OrderLineItemAdminInline(admin.TabularInline):
    ''' Define the OrderLineItem admin inline '''
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)

class OrderAdmin(admin.ModelAdmin):
    ''' Define the order admin '''
    inlines = (OrderLineItemAdminInline,)
    readonly_fields = ('order_ref', 'date', 'delivery_cost', 'order_total', 'grand_total',
                        'original_cart', 'stripe_pid',)
    fields = ('order_ref', 'user_profile', 'date', 'full_name', 'email', 'phone_number', 'country',
                'postcode', 'town_or_city', 'street_address1', 'street_address2', 'county',
                'delivery_cost', 'order_total', 'grand_total', 'original_cart', 'stripe_pid',)
    list_display = ('order_ref', 'date', 'full_name',
                    'order_total', 'delivery_cost', 'grand_total',)

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)
