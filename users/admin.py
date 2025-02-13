from django.contrib import admin

from carts.admin import CartTabAdmin
from orders.admin import OrderTabAdmin
from .models import Adress, User

@admin.register(Adress)
class AdressAdmin(admin.ModelAdmin):
    list_display = ('id', 'city', 'street', 'house', 'apartment', 'user')
    list_display_links = ('id', 'city')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','phone', 'is_staff', 'get_groups')
    list_display_links = ('id', 'phone')

    inlines = [CartTabAdmin, OrderTabAdmin]

    def get_groups(self, obj):
        return ", ".join([group.name for group in obj.groups.all()])  # Получаем имена групп пользователя
    get_groups.short_description = 'Группы'  # Заголовок столбца
