from email.mime import image
from django.conf.locale import sl
from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True, verbose_name='URL')
    image = models.ImageField(upload_to='categories', blank=True, null=True, verbose_name='Изображение', )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
            return self.name
