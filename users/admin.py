from django.contrib import admin
from .models import Adress, User

@admin.register(Adress)
class AdressAdmin(admin.ModelAdmin):
    list_display = ('id', 'city', 'street', 'house', 'apartment', 'user')
    list_display_links = ('id', 'city')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','phone')
    list_display_links = ('id', 'phone')


