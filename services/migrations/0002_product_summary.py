# Generated by Django 4.2.13 on 2024-08-20 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='summary',
            field=models.TextField(blank=True),
        ),
    ]
