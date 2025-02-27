from typing import Literal
from django.contrib import admin

from goods.models import Categories, Products

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name',]


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields: dict[str, tuple[Literal['name']]] = {'slug': ('name',)}
    list_display = ['name', 'quantity', 'price', 'discount',]
    list_editable = ['discount',]
    search_fields = ['name', 'description',]
    list_filter = ['quantity', 'category', 'discount',]
    fields = [
        'name',
        'category',
        'slug',
        'description',
        'image', 
        ('price', 'discount'),
        'quantity',
    ]
