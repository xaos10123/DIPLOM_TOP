from django.contrib import admin

from carts.models import Cart

class CartTabAdmin(admin.TabularInline):
    model = Cart
    fields = ('product', 'quantity',)
    search_fields = ('product__name',)
    extra = 1
    
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'quantity', 'created_timeestamp',)
    list_filter = ('user', 'product', 'created_timeestamp',)
    search_fields = ('user__username', 'product__name')
    ordering = ('-created_timeestamp',)
