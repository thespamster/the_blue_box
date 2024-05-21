'''
    This file contains the model for the Doctors table.
'''

from django.db import models

# Create your models here.

class Doctors(models.Model):
    ''' Model for the Doctors table ''' 
    name = models.CharField(max_length=254)

    class Meta:
        ''' Meta class for the Doctors model'''
        verbose_name_plural = 'Doctors'

    def __str__(self):
        return self.name
    