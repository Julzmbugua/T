# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-12 06:12
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0020_auto_20170911_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
