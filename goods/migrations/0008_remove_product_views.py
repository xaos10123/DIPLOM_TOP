# Generated by Django 5.1.4 on 2025-01-13 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0007_product_order_amount_product_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='views',
        ),
    ]
