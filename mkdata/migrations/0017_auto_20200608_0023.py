# Generated by Django 2.1.15 on 2020-06-07 15:23
from django.core.management import call_command
from django.db import migrations

def load_fixture(apps, schema_editor):
    call_command('loaddata', 'mkdata/fixture/works_ver06.json', app_label='mkdata')


class Migration(migrations.Migration):

    dependencies = [
        ('mkdata', '0016_auto_20200607_2212'),
    ]

    operations = [
        migrations.RunPython(load_fixture),
    ]