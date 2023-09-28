# Generated by Django 4.2.4 on 2023-08-16 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0006_remove_green_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='green',
            name='first_name',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='green',
            name='is_activae',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='green',
            name='last_name',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]