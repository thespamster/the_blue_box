'''
This file is used to initialize the fanart app configuration.
'''

from django.apps import AppConfig


class FanartConfig(AppConfig):
    ''' Initialize the fanart app configuration '''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fanart'
