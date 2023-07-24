# Generated by Django 4.2.3 on 2023-07-24 09:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eloquent_app', '0003_remove_device_field_1_remove_device_field_10_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Owner'),
        ),
    ]
