# Generated by Django 4.2.13 on 2024-08-28 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_appointment_appointment_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='accepted_date',
        ),
    ]
