# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-12 08:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sprinkler', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheduler',
            name='skip_days',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='sprinkler',
            name='GPIO_pin',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='sprinkler',
            name='notes',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='sprinkler',
            name='duration',
            field=models.IntegerField(default=0),
        ),
    ]
