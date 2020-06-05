# Generated by Django 2.1.15 on 2020-06-02 18:57
from django.core.management import call_command
from django.db import migrations

def load_fixture(apps, schema_editor):
    call_command('loaddata', 'mkdata/fixture/works_ver01.json', app_label='mkdata')

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mkdata', '0009_auto_20200529_1422'),
    ]

    operations = [
        migrations.RunPython(load_fixture),
    ]