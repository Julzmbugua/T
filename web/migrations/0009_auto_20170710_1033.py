# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-10 07:33
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_carouselcaption_caption_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carouselcover',
            name='displayed',
        ),
        migrations.AddField(
            model_name='carouselcover',
            name='slide',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='portfoliographic',
            name='graphic',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='web/media/'), upload_to=b''),
        ),
    ]