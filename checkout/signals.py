'''
    Signals are used to update the order total when a line item is added or removed from the order.
'''

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import OrderLineItem

@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, **kwargs):
    ''' update order total on lineitem save '''
    instance.order.update_total()

@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    ''' update order total on lineitem delete '''
    instance.order.update_total()
