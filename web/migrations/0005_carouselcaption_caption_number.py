# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-08 11:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20170708_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='carouselcaption',
            name='caption_number',
            field=models.IntegerField(default=1, unique=True),
            preserve_default=False,
        ),
    ]
