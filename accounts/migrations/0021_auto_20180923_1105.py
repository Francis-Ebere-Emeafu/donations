# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-09-23 11:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_auto_20180906_0536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='membership',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.Membership'),
            preserve_default=False,
        ),
    ]
