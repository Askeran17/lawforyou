# Generated by Django 4.2.13 on 2024-09-07 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0010_alter_product_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='url',
            field=models.SlugField(max_length=300, null=True, unique=True),
        ),
    ]