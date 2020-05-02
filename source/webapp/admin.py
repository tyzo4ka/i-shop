from django.contrib import admin
from webapp.models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'category_name']
    list_filter = ['category_name']
    list_display_links = ['pk', 'category_name']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'category', 'price', 'in_stock']
    list_filter = ['name', 'category', 'price', 'in_stock']
    list_display_links = ['name', 'category', 'price', 'in_stock']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

