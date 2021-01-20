# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-08-05 10:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('message_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
