# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-02 19:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sprinkler', '0005_weather'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weather',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True),
        ),
    ]
