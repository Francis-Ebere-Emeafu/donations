# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-08-23 09:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_newspost_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='newspost',
            name='text_content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
