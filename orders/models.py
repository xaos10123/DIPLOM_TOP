from django.db import models

from goods.models import Product
from users.models import Adress, User

class OrderItemQueryset(models.QuerySet):

    def total_price(self):
        return sum(cart.total_price for cart in self)
    
    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        else:
            return 0
    


class Order(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.SET_DEFAULT, verbose_name='Пользователь', default=None, blank=True, null=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    adress = models.ForeignKey(to=Adress, on_delete=models.SET_DEFAULT, verbose_name='Адрес', default=None)
    is_paid = models.BooleanField(default=False, verbose_name='Статус оплаты')
    status = models.CharField(max_length=50, default='В обработке', verbose_name='Статус заказа')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ №{self.pk} | {self.user.username} | {self.created_timestamp}'
    
class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, verbose_name='Заказ', related_name='items')
    product = models.ForeignKey(to=Product, on_delete=models.SET_DEFAULT, verbose_name='Товар', null=True, default=None)
    name = models.CharField(max_length=255, verbose_name='Название')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    price = models.PositiveIntegerField(default=0, verbose_name='Цена')
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата продажи')

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'

    objects = OrderItemQueryset.as_manager()

    def products_price(self):
        return self.quantity * self.price

    def __str__(self):
        return f'Заказ № {self.pk} : {self.name} | {self.quantity}шт. | {self.price}₽'
        
