# Generated by Django 4.2.7 on 2024-01-07 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_services_header'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='img',
        ),
    ]