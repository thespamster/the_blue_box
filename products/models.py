'''
    This file contains the models for the products app. The Category model and Product model
'''

from django.db import models

# Create your models here.

class Category(models.Model):
    ''' Model for the product categories '''
    class Meta:
        ''' Meta class for the category model '''
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_display_name(self):
        ''' return the display name of the category '''
        return self.display_name


class Product(models.Model):
    ''' Model for the products '''
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    ean = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=254, null=True, blank=True)
    tags = models.CharField(max_length=254)

    def __str__(self):
        return self.name
    