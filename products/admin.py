from django.contrib import admin
from .models import Product, Category

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
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
    list_display = (
        'name',
        'display_name',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

