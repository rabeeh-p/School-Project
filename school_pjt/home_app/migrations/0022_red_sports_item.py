# Generated by Django 4.2.4 on 2023-08-18 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0021_blue_sports_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='red',
            name='sports_item',
            field=models.BooleanField(default=False),
        ),
    ]
