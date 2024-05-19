'''
    Django admin class for products app.
'''

from django.contrib import admin
from .models import Product, Category

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    ''' Define the product admin '''
    list_display = (
        'ean',
        'name',
        'category',
        'price',
        'rating',
        'image',
        'tags',
    )
    ordering = ('name',)

class CategoryAdmin(admin.ModelAdmin):
    ''' Define the category admin '''
    list_display = (
        'name',
        'display_name',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
