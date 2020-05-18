from django.db import models


# Create your models here.

class Work(models.Model):
    name = models.CharField(max_length=200)
    num_of_data = models.IntegerField(default=0)

    #sum of the assessment values for all users is recorded

    like = models.IntegerField(default=0)
    joy = models.IntegerField(default=0)
    anger = models.IntegerField(default=0)
    sadness = models.IntegerField(default=0)
    fun = models.IntegerField(default=0)
    tech_constitution = models.IntegerField(default=0)
    tech_story = models.IntegerField(default=0)
    tech_character = models.IntegerField(default=0)
    tech_speech = models.IntegerField(default=0)
    tech_picture = models.IntegerField(default=0)

    def __str__(self):
        return self.name
