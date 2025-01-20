from django.db import models

from goods.models import Product
from users.models import User


class CartQueryset(models.QuerySet):
    def total_price(self):
        return sum(cart.products_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Cart(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="carts",
        blank=True,
        null=True,
        verbose_name="Пользователь",
    )
    product = models.ForeignKey(
        to=Product, on_delete=models.CASCADE, related_name="carts", verbose_name="Товар"
    )
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество")
    session_key = models.CharField(max_length=40, blank=True, null=True)
    created_timeestamp = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата добавления"
    )

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"

    objects = CartQueryset.as_manager()

    def products_price(self):
        return self.product.sell_price() * self.quantity

    def __str__(self):
        return f"{self.user} - {self.product} - {self.quantity}"
