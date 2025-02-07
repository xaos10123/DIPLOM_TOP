from django.contrib import admin

from promotions.models import Promo

@admin.register(Promo)
class PromoAdmin(admin.ModelAdmin):
    list_display = ('promo_name', 'promo_color', 'promo_start_date', 'promo_end_date', 'promo_discount', 'promo_status')
    list_filter = ('promo_status',)
    search_fields = ('promo_name',)
    date_hierarchy = 'promo_start_date'
    ordering = ('-promo_start_date',)
    fieldsets = (
        (None, {
            'fields': ('promo_name', 'promo_color', 'promo_description', 'promo_image', 'promo_start_date', 'promo_end_date', 'promo_discount', 'promo_status', 'promo_products')
        }),
    )
    filter_horizontal = ('promo_products',)
    actions = ('make_active', 'make_inactive')
