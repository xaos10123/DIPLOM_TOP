from django.contrib.auth.models import AbstractUser
from django.db import models


class Adress(models.Model):
    city = models.CharField(max_length=255, verbose_name="Город")
    street = models.CharField(max_length=255, verbose_name="Улица")
    house = models.CharField(max_length=255, verbose_name="Дом")
    apartment = models.CharField(max_length=255, verbose_name="Квартира")

    class Meta:
        verbose_name = "Адрес"
        verbose_name_plural = "Адреса"

    def __str__(self):
        return self.city + " " + self.street + " " + self.house + " " + self.apartment


class User(AbstractUser):
    adress = models.ForeignKey(Adress, on_delete=models.CASCADE, verbose_name="Адрес", null=True, blank=True)
    phone = models.CharField(max_length=255, verbose_name="Телефон", unique=True)

    USERNAME_FIELD = 'phone'

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username
