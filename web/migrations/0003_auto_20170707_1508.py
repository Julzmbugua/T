# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-07 12:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20170704_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='carouselcover',
            name='displayed',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='carouselcover',
            name='cover',
            field=models.ImageField(upload_to='backgrounds'),
        ),
    ]
