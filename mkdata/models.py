from django.db import models


# Create your models here.

class Work(models.Model):
    name = models.CharField(max_length=200)
    like_average = models.FloatField(default=0)
    joy = models.FloatField(default=0)
    anger = models.FloatField(default=0)
    sadness = models.FloatField(default=0)
    fun = models.FloatField(default=0)
    tech_constitution = models.FloatField(default=0)
    tech_story = models.FloatField(default=0)
    tech_character = models.FloatField(default=0)
    tech_speech = models.FloatField(default=0)
    tech_picture = models.FloatField(default=0)

    def __str__(self):
        return self.name
