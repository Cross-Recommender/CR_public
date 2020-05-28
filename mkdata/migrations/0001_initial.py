# Generated by Django 2.1.15 on 2020-05-17 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='works',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('like_average', models.IntegerField(default=0)),
                ('joy', models.IntegerField(default=0)),
                ('anger', models.IntegerField(default=0)),
                ('sadness', models.IntegerField(default=0)),
                ('fun', models.IntegerField(default=0)),
                ('tech_constitution', models.IntegerField(default=0)),
                ('tech_story', models.IntegerField(default=0)),
                ('tech_character', models.IntegerField(default=0)),
                ('tech_speech', models.IntegerField(default=0)),
                ('tech_picture', models.IntegerField(default=0)),
            ],
        ),
    ]
