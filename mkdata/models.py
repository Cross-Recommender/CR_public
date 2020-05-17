from django.db import models

# Create your models here.

class works(models.Model):
    name = models.CharFielf(max_length = 200)
    like_average = model.IntegerField(default = 0)
    joy = model.IntegerField(default = 0)
    anger = model.IntegerField(default = 0)
    sadness = model.IntegerField(default=0)
    fun = model.IntegerField(default = 0)
    tech_constitution = model.IntegerField(default = 0)
    tech_story = model.IntegerField(default = 0)
    tech_character = model.IntegerField(default = 0)
    tech_speech = model.IntegerField(default = 0)
    tech_picture = model.IntegerField(default = 0)