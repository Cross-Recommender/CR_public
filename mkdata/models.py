from django.db import models


# Create your models here.

class Work(models.Model):
    name = models.CharField(max_length=200)
    num_of_data = models.IntegerField(default=0)

    # sum of the assessment values for all users is recorded

    like = models.FloatField(default=0)
    joy = models.FloatField(default=0)
    anger = models.FloatField(default=0)
    sadness = models.FloatField(default=0)
    fun = models.FloatField(default=0)
    tech_constitution = models.FloatField(default=0)
    tech_story = models.FloatField(default=0)
    tech_character = models.FloatField(default=0)
    tech_speech = models.FloatField(default=0)
    tech_picture = models.FloatField(default=0)

    #映画特有の技術的評価軸
    mov_tech_audio = models.FloatField(default=0)
    mov_tech_acting = models.FloatField(default=0)

    ###ジャンルを表す　1: 漫画　2: 映画
    genre = models.IntegerField(default=1)

    ### url
    url = models.CharField(default="0", max_length=300)

    def __str__(self):
        return self.name

    def get_average(self):
        if self.num_of_data == 0:
            return None
        average = list(map(lambda x: x / self.num_of_data,
                           [self.joy,self.anger,self.sadness,self.fun,self.tech_constitution,self.tech_story,self.tech_character,self.tech_speech,self.tech_picture]))
        return average

    '''
    def get_evaluation_item(self, num):
        if num == 0:
            return self.joy
        elif num == 1:
            return self.anger
        elif num == 2:
            return self.sadness
        elif num == 3:
            return self.fun
        elif num == 4:
            return self.tech_constitution
        elif num == 5:
            return self.tech_story
        elif num == 6:
            return self.tech_character
        elif num == 7:
            return self.tech_speech
        elif num == 8:
            return self.tech_picture
        elif num == 9:
            return self.tech_audio
        elif num == 10:
            return self.tech_acting
    '''

def try_Work_get(id):
    try:
        return Work.objects.get(id=id)
    except Work.DoesNotExist:
        return None

# mkbaseworksはrecommend.pyに引っ越しました



class AddedWork(models.Model):
    name = models.CharField(max_length=200)
    userid = models.IntegerField(default=0)
    genre = models.IntegerField(default=1)

    # sum of the assessment values for all users is recorded

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
    tech_audio = models.IntegerField(default=0)
    tech_acting = models.IntegerField(default=0)

    def __str__(self):
        return self.name
