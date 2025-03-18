# Generated by Django 5.1.4 on 2025-03-18 14:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_orderitem_product'),
        ('users', '0005_user_age_confirmed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='adress',
            field=models.ForeignKey(default='Адрес не указан', on_delete=django.db.models.deletion.SET_DEFAULT, to='users.adress', verbose_name='Адрес'),
        ),
    ]
