# Generated by Django 2.1.15 on 2020-05-27 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mkdata', '0007_addedwork'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addedwork',
            old_name='user',
            new_name='userid',
        ),
    ]
