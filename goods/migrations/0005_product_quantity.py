# Generated by Django 5.1.4 on 2025-01-11 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_remove_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество'),
        ),
    ]
