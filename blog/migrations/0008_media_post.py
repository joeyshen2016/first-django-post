# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-13 05:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20161013_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='medias', to='blog.Post'),
            preserve_default=False,
        ),
    ]
