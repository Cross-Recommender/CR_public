# Generated by Django 2.1.15 on 2020-05-29 05:22
from django.core.management import call_command
from django.db import migrations

def load_fixture(apps, schema_editor):
    call_command('loaddata', 'mkdata/fixture/work.json', app_label='mkdata')

class Migration(migrations.Migration):

    dependencies = [
        ('mkdata', '0008_auto_20200527_2246'),
    ]

    operations = [
        migrations.RunPython(load_fixture),
    ]
