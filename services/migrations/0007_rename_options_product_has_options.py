# Generated by Django 4.2.13 on 2024-09-01 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_alter_review_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='options',
            new_name='has_options',
        ),
    ]
