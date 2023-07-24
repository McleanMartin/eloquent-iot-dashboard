# Generated by Django 4.2.3 on 2023-07-23 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Device Name', max_length=60, verbose_name='Device Name')),
                ('field_1', models.CharField(blank=True, max_length=20, null=True, verbose_name='Field 1')),
                ('field_id_1', models.CharField(blank=True, max_length=30, null=True, verbose_name='Field ID 1')),
                ('field_2', models.CharField(blank=True, max_length=20, null=True, verbose_name='Field 2')),
                ('field_id_2', models.CharField(blank=True, max_length=30, null=True, verbose_name='Field ID 2')),
                ('field_3', models.CharField(blank=True, max_length=20, null=True, verbose_name='Field 3')),
                ('field_id_3', models.CharField(blank=True, max_length=30, null=True, verbose_name='Field ID 3')),
                ('field_4', models.CharField(blank=True, max_length=20, null=True, verbose_name='Field 4')),
                ('field_id_4', models.CharField(blank=True, max_length=30, null=True, verbose_name='Field ID 4')),
                ('field_5', models.CharField(blank=True, max_length=20, null=True, verbose_name='Field 5')),
                ('field_id_5', models.CharField(blank=True, max_length=30, null=True, verbose_name='Field ID 5')),
                ('field_6', models.CharField(blank=True, max_length=20, null=True, verbose_name='Field 6')),
                ('field_id_6', models.CharField(blank=True, max_length=30, null=True, verbose_name='Field ID 6')),
                ('field_7', models.CharField(blank=True, max_length=20, null=True, verbose_name='Field 7')),
                ('field_id_7', models.CharField(blank=True, max_length=30, null=True, verbose_name='Field ID 7')),
                ('field_8', models.CharField(blank=True, max_length=20, null=True, verbose_name='Field 8')),
                ('field_id_8', models.CharField(blank=True, max_length=30, null=True, verbose_name='Field ID 8')),
                ('field_9', models.CharField(blank=True, max_length=20, null=True, verbose_name='Field 9')),
                ('field_id_9', models.CharField(blank=True, max_length=30, null=True, verbose_name='Field ID 9')),
                ('field_10', models.CharField(blank=True, max_length=20, null=True, verbose_name='Field 10')),
                ('field_id_10', models.CharField(blank=True, max_length=30, null=True, verbose_name='Field ID 10')),
                ('api_key', models.CharField(max_length=200, verbose_name='Api key')),
                ('description', models.TextField(blank=True, max_length=255, verbose_name='Description')),
                ('enable', models.BooleanField(default=True, verbose_name='Enable')),
                ('remote_address', models.CharField(max_length=255, verbose_name='Ip Address')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='Publish Date')),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
    ]
