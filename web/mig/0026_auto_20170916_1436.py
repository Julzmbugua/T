# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-16 11:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0025_auto_20170916_1419'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='blog',
            name='tags',
        ),
        migrations.AddField(
            model_name='blog',
            name='b_tags',
            field=models.ManyToManyField(related_name='_blog_b_tags_+', to='web.Blog'),
        ),
        migrations.AddField(
            model_name='tag',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Blog'),
        ),
    ]