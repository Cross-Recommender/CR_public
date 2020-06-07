# Generated by Django 2.1.15 on 2020-06-07 13:12
from django.core.management import call_command
from django.db import migrations

def load_fixture(apps, schema_editor):
    call_command('loaddata', 'mkdata/fixture/works_ver03.json', app_label='mkdata')
    call_command('loaddata', 'mkdata/fixture/works_ver04.json', app_label='mkdata')
    call_command('loaddata', 'mkdata/fixture/works_ver05.json', app_label='mkdata')


class Migration(migrations.Migration):

    dependencies = [
        ('mkdata', '0015_work_url'),
    ]

    operations = [
        migrations.RunPython(load_fixture),
    ]
