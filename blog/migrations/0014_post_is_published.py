# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-04 07:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_post_is_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
    ]
