# Generated by Django 5.1.4 on 2025-02-07 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('promotions', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='promo',
            options={'verbose_name': 'Акция', 'verbose_name_plural': 'Акции'},
        ),
    ]
