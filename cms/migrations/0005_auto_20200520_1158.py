# Generated by Django 2.1.15 on 2020-05-20 02:58

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0004_auto_20200520_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='work_like',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=0), default=list, size=2),
        ),
    ]
