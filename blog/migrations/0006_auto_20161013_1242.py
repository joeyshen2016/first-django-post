# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-13 04:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20161013_1134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='post',
        ),
        migrations.DeleteModel(
            name='ProfileImage',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]