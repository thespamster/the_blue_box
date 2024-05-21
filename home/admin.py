'''
    This file is used to register the models in the admin panel. 

'''

from django.contrib import admin
from home.models import Doctors

# Register your models here.
class DoctorsAdmin(admin.ModelAdmin):
    ''' Define the Doctors admin '''
    list_display = (
        'pk_doctor',
        'name',
    )

admin.site.register(Doctors, DoctorsAdmin)
