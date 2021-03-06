# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-07 09:48
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0017_auto_20170906_1831'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pictures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture_name', models.CharField(max_length=100)),
                ('picture', models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='web/media/'), upload_to='')),
                ('picture_url', models.URLField(max_length=100)),
                ('picture_no', models.IntegerField(unique=True)),
                ('upload_date', models.DateTimeField()),
            ],
        ),
    ]
