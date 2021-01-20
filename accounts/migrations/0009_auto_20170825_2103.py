# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-08-25 21:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20170824_1347'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='giftoptions',
            options={'verbose_name_plural': 'Gift Options'},
        ),
        migrations.AddField(
            model_name='giftoptions',
            name='dollar_value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
    ]