# Generated by Django 5.0.7 on 2024-07-30 01:06

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
