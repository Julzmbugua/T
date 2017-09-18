# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-16 11:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0024_auto_20170916_1412'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog_tags',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='tags',
        ),
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(related_name='_blog_tags_+', to='web.Blog'),
        ),
        migrations.DeleteModel(
            name='Blog_tags',
        ),
    ]
