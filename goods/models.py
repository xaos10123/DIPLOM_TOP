from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название")
    slug = models.SlugField(
        max_length=150, unique=True, blank=True, null=True, verbose_name="URL"
    )
    image = models.ImageField(
        upload_to="categories",
        blank=True,
        null=True,
        verbose_name="Изображение",
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    char = models.CharField(max_length=100, verbose_name="Характеристика")
    slug = models.SlugField(
        max_length=150, unique=True, blank=True, null=True, verbose_name="URL"
    )
    image = models.ImageField(
        upload_to="products", blank=True, null=True, verbose_name="Изображение"
    )
    price = models.IntegerField(verbose_name="Цена")
    discaunt = models.IntegerField(default=0, verbose_name="Скидка по акциям")
    category = models.ForeignKey(
        Categories, on_delete=models.PROTECT, verbose_name="Категория"
    )
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество")
    order_amount = models.PositiveIntegerField(
        default=0, verbose_name="Количество заказов"
    )
    # views = models.PositiveIntegerField(default=0, verbose_name='Просмотров')

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        unique_together = ["name", "char"]
        ordering = ["name", "char"]
        default_related_name = "products"

    def __str__(self):
        return f"{self.name} {self.char}"

    def sell_price(self):
        if self.discaunt > 0:
            return int(self.price - self.price * self.discaunt / 100)
        else:
            return self.price
