from django.contrib import admin

from .models import Categories, Product

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'image')
    list_display_links = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('order_amount', 'discaunt',)
    list_display = ('id', 'name', 'char', 'quantity', 'price', 'category',  'discaunt',)
    list_display_links = ('id', 'name', 'char')
    prepopulated_fields = {'slug': ('name', 'char',)}

