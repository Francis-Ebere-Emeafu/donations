# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-08-26 07:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20170826_0720'),
    ]

    operations = [
        migrations.AddField(
            model_name='gift',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]