# Generated by Django 4.2.4 on 2023-08-17 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0013_studentevnt'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]
