from django.db import models
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from goods.models import Product


class Promo(models.Model):
    promo_name = models.CharField(max_length=255, verbose_name="Название акции")
    promo_description = models.TextField(verbose_name="Описание акции")
    promo_image = models.ImageField(
        upload_to="promos/", verbose_name="Изображение акции"
    )
    promo_start_date = models.DateField(verbose_name="Дата начала акции")
    promo_end_date = models.DateField(verbose_name="Дата окончания акции")
    promo_discount = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name="Скидка"
    )
    promo_status = models.BooleanField(default=True, verbose_name="Статус")
    promo_products = models.ManyToManyField(Product, verbose_name="Товары")

    class Meta:
        verbose_name = "Акция"
        verbose_name_plural = "Акции"


@receiver(m2m_changed, sender=Promo.promo_products.through)
def update_product_discount(sender, instance, action, pk_set, **kwargs):
    if action == "post_add":
        for product in Product.objects.filter(id__in=pk_set):
            if int(instance.promo_discount) > product.discaunt:
                product.discaunt = int(instance.promo_discount)
                product.save()
