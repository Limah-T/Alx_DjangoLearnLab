# Generated by Django 5.1.6 on 2025-03-29 14:04

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
