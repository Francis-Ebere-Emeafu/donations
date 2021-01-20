# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-10-01 14:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('convention', '0002_attendee'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentDelegate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=80)),
                ('school', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=150)),
                ('level', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=50)),
                ('address', models.TextField(blank=True)),
                ('extra_info', models.TextField(blank=True)),
                ('when', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'Students delegate',
            },
        ),
    ]
