# Generated by Django 4.2.13 on 2024-09-15 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0002_alter_lawfaq_options_lawfaq_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lawfaq',
            options={'ordering': ['faq_item'], 'verbose_name_plural': 'FAQS'},
        ),
        migrations.RenameField(
            model_name='lawfaq',
            old_name='number',
            new_name='faq_item',
        ),
    ]
