'''
This file is used to configure the app name for the cart app.
'''

from django.apps import AppConfig


class CartConfig(AppConfig):
    ''' Initialize the cart app configuration '''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cart'
