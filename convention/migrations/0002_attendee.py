# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-08-22 12:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convention', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=75)),
                ('address', models.TextField(blank=True)),
                ('bio', models.TextField(blank=True)),
            ],
        ),
    ]
