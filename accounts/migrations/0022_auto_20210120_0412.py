# Generated by Django 2.2.17 on 2021-01-20 04:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_auto_20180923_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='membership',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Membership'),
        ),
        migrations.AlterField(
            model_name='renewal',
            name='account',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Account'),
        ),
    ]
