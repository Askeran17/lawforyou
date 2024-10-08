# Generated by Django 4.2.13 on 2024-09-16 20:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0008_remove_product_has_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(1)]),
        ),
        migrations.AlterField(
            model_name='product',
            name='item',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='url',
            field=models.SlugField(max_length=300, null=True, unique=True),
        ),
    ]
