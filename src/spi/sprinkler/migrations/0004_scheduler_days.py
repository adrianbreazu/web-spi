# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-12 12:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sprinkler', '0003_auto_20160812_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheduler',
            name='days',
            field=models.CharField(default='MTWTFSS', max_length=7),
        ),
    ]