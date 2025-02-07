# Generated by Django 5.1.4 on 2025-02-07 05:04

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('promotions', '0002_alter_promo_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='promo',
            name='promo_color',
            field=colorfield.fields.ColorField(blank=True, default='#acd5f5fc', image_field=None, max_length=25, null=True, samples=None, verbose_name='Цвет фона акции'),
        ),
    ]
