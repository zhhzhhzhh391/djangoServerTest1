# Generated by Django 3.2.7 on 2022-04-16 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0009_alter_user_headicon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='headicon',
            field=models.BinaryField(default=None, max_length=254, verbose_name='存储图片'),
        ),
    ]
