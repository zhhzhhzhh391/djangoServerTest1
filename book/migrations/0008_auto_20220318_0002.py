# Generated by Django 3.2.7 on 2022-03-17 16:02

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_auto_20220317_2356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='status',
        ),
    ]
