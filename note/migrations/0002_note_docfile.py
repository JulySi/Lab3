# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-25 19:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='docfile',
            field=models.FileField(default='', upload_to='documents/%Y/%m/%d'),
        ),
    ]
