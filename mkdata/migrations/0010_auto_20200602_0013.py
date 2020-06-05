# Generated by Django 2.1.15 on 2020-06-01 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mkdata', '0008_auto_20200527_2246'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='genre',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='work',
            name='mov_tech_acting',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='work',
            name='mov_tech_audio',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='work',
            name='anger',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='work',
            name='fun',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='work',
            name='joy',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='work',
            name='like',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='work',
            name='sadness',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='work',
            name='tech_character',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='work',
            name='tech_constitution',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='work',
            name='tech_picture',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='work',
            name='tech_speech',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='work',
            name='tech_story',
            field=models.FloatField(default=0),
        ),
    ]