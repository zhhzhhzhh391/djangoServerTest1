# Generated by Django 3.2.7 on 2022-03-15 12:56

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_auto_20220315_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='userfriendlist',
            name='User',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='book.user', verbose_name='外键User'),
            preserve_default=False,
        ),
    ]
