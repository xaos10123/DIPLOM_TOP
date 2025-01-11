# Generated by Django 5.1.4 on 2025-01-11 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterField(
            model_name='categories',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='categories', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='slug',
            field=models.SlugField(blank=True, max_length=150, null=True, unique=True, verbose_name='URL'),
        ),
    ]
