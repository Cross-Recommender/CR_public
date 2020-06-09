# Generated by Django 2.1.15 on 2020-06-07 16:54

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20200608_0132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='evaluation_avg',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(default=0), default=list, null=True, size=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='evaluation_std',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(default=0), default=list, null=True, size=20),
        ),
    ]