# Generated by Django 4.2.7 on 2024-01-07 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_portfolio_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='price',
            name='title',
        ),
        migrations.AddField(
            model_name='price',
            name='price',
            field=models.TextField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
