# Generated by Django 4.2.4 on 2023-08-17 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0016_sportsmembers'),
    ]

    operations = [
        migrations.AddField(
            model_name='sportsmembers',
            name='role',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
