# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-16 11:12
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0023_auto_20170916_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='tags',
            field=django.contrib.postgres.fields.jsonb.JSONField(),
        ),
    ]
