# Generated by Django 4.2.13 on 2024-09-07 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_order_user_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderlineitem',
            name='product_option',
        ),
    ]