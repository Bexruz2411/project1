# Generated by Django 4.2.7 on 2024-01-07 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_about_icon_remove_services_icon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='header',
        ),
    ]
