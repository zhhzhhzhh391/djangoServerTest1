# Generated by Django 3.2.7 on 2022-04-17 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0010_alter_user_headicon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='headicon',
            field=models.TextField(default=None, verbose_name='存储图片'),
        ),
    ]
