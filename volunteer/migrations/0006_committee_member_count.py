# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2019-01-08 22:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0005_committee'),
    ]

    operations = [
        migrations.AddField(
            model_name='committee',
            name='member_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]