# Generated by Django 3.2.7 on 2022-03-21 14:08

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0010_auto_20220319_2223'),
    ]

    operations = [

        migrations.AddField(
            model_name='userfriendlist',
            name='groupName',
            field=models.CharField(default=None, max_length=254, verbose_name='好友频道名'),
            preserve_default=False,
        ),

    ]
