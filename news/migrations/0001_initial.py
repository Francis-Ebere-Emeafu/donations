# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-08-05 10:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('reference_date', models.DateField()),
                ('publish_date', models.DateField()),
                ('active', models.BooleanField(default=False)),
            ],
        ),
    ]