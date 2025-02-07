from django.db import migrations
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from orders.models import Order

def create_courier_group(apps, schema_editor):
    courier_group, created = Group.objects.get_or_create(name='Courier')
    
    order_content_type = ContentType.objects.get_for_model(Order)
    
    courier_permissions = [
        Permission.objects.get_or_create(
            codename='can_view_orders',
            name='Может видеть заказы',
            content_type=order_content_type,
        )[0],
        Permission.objects.get_or_create(
            codename='can_update_order_status',
            name='Может обновлять статус заказа',
            content_type=order_content_type,
        )[0],
    ]
    
    courier_group.permissions.add(*courier_permissions)

def remove_courier_group(apps, schema_editor):
    Group.objects.filter(name='Courier').delete()

class Migration(migrations.Migration):
    dependencies = [
        ('users', '0003_adress_is_active'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_courier_group, remove_courier_group),
    ]
