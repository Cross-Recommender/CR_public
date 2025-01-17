# Generated by Django 2.1.15 on 2020-06-07 16:19

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0012_auto_20200607_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='evaluation_avg',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), null=True, size=100000),
        ),
        migrations.AddField(
            model_name='user',
            name='evaluation_std',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), null=True, size=100000),
        ),
    ]
