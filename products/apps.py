'''
    This file is used to configure the app name for the products app.
'''

from django.apps import AppConfig

class ProductsConfig(AppConfig):
    ''' Initialize the products app configuration '''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'
