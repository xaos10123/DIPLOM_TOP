from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, phone, password=None, **extra_fields):
        if not phone:
            raise ValueError("Номер телефона обязателен для заполнения")

        user = self.model(phone=phone, username=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(phone, password, **extra_fields)


class User(AbstractUser):
    phone = models.CharField(max_length=255, verbose_name="Телефон", unique=True)
    age_confirmed = models.BooleanField(verbose_name="Возраст больше 18 подтвержден", default=False, blank=True)

    USERNAME_FIELD = "phone"
    objects = CustomUserManager()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"(id:{self.pk}) {self.username}"


class Adress(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="addresses",
        verbose_name="Пользователь",
        null=True,
        blank=True,
    )
    city = models.CharField(max_length=255, verbose_name="Город")
    street = models.CharField(max_length=255, verbose_name="Улица")
    house = models.CharField(max_length=255, verbose_name="Дом")
    apartment = models.CharField(max_length=255, verbose_name="Квартира")
    is_active = models.BooleanField(
        default=False, verbose_name="Активность", null=True, blank=True
    )

    class Meta:
        verbose_name = "Адрес"
        verbose_name_plural = "Адреса"

    def __str__(self):
        return f"г.{self.city} ул.{self.street} дом {self.house} кв.{self.apartment}"
