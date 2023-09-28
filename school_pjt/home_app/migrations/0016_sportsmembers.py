# Generated by Django 4.2.4 on 2023-08-17 09:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0015_sports_image_sports_place'),
    ]

    operations = [
        migrations.CreateModel(
            name='SportsMembers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sports', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_app.sports')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]