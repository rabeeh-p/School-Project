# Generated by Django 4.2.4 on 2023-08-17 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0014_sports'),
    ]

    operations = [
        migrations.AddField(
            model_name='sports',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='sports',
            name='place',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
