# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-09-06 05:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_account_certificate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Renewal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='next_payment_due',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='renewal',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Account'),
        ),
    ]
