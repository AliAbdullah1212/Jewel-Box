# Generated by Django 4.2.13 on 2024-06-03 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_order_sale_price_alter_order_total_cost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='is_setting',
            new_name='is_set',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='setting_detail',
            new_name='set_detail',
        ),
    ]
