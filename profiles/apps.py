'''
    Django configuration file for profiles app
'''

from django.apps import AppConfig

class ProfilesConfig(AppConfig):
    ''' Initialize the profiles app configuration '''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'
