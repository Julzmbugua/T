# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-11 13:14
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0019_auto_20170907_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
