# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-02 20:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sprinkler', '0007_auto_20160902_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weather',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]