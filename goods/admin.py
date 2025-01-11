from django.contrib import admin

from .models import Categories

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'image')
    list_display_links = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}
