# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-10 02:07
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20171109_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolioitem',
            name='display_image',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/portfolio'), upload_to=''),
        ),
    ]
