from django.db import models

from goods.models import Product

class Promo(models.Model):
    promo_name = models.CharField(max_length=255, verbose_name='Название акции')
    promo_description = models.TextField(verbose_name='Описание акции')
    promo_image = models.ImageField(upload_to='promos/', verbose_name='Изображение акции')
    promo_start_date = models.DateField(verbose_name='Дата начала акции')
    promo_end_date = models.DateField(verbose_name='Дата окончания акции')
    promo_discount = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Скидка')
    promo_status = models.BooleanField(default=True, verbose_name='Статус')
    promo_products = models.ManyToManyField(Product, verbose_name='Товары')

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'
# 