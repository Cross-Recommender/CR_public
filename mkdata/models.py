from django.db import models
import  random


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

    def __str__(self):
        return self.name

    def get_average(self):
        if self.num_of_data == 0:
            return None
        average = list(map(lambda x: x / self.num_of_data,
                           [self.joy,self.anger,self.sadness,self.fun,self.tech_constitution,self.tech_story,self.tech_character,self.tech_speech,self.tech_picture]))
        return average



# work_like を元にユーザーの高評価作品順に並んだ　works　を返す
# 都合がいいので仮置き　cms/views.py で使用
def mkbaseWorks(string):
    """
    work_like をもとにユーザーの高評価作品順に並んだ　works　を返す
    評価点が同じ作品の順序はランダムに決まる
    この関数を呼び出すたびに順番は変わる
    ・Work.objects.count()は必ずしもWorkのidの最大値に一致するとは限らない
    (削除されたオブジェクトがあったときに, そのオブジェクトのidは補間されないので,
     idを飛ばしてオブジェクトが設定される場合が存在する)

    ・work_likeはデフォルトで各作品について'0'で設定しているので, 仮に
    Works = list(map(lambda x: Work.objects.get(id=x), arr))
    において指定したidに対応するオブジェクトが(上と同じ理由で)存在していなかった場合にバグってしまう

    ・enumerateはindexを0から指定するのに対して, idは1からスタートする

    以上を踏まえて若干修正します。

    追記(20200524/12:40)
    · enumerateは第二引数で1から開始するよう指定しているのでそれに合わせて修正しました
    · 例外処理を加えました
    · 降順にするのを忘れていたので降順にしました
    """

    '''
    arr = list(map(lambda x: int(x), list(string[:Work.objects.count()])))
    arr = list(enumerate(arr, 1))
    arr.sort(key=lambda x: x[1])
    arr = list(map(lambda x: x[0], arr))
    Works = list(map(lambda x: Work.objects.get(id=x), arr))
    '''
    arr = list(map(lambda x: int(x)+random.random(), list(string[:Work.objects.all().order_by("-id")[0].id])))
    arr = list(enumerate(arr, 1))
    arr.sort(key=lambda x: x[1], reverse=True)
    arr = [x for x in arr if x[1] >= 1]
    arr = list(map(lambda x: x[0], arr))
    #print(arr)
    ###次の行に修正の必要あり(idが取得できなかった場合の例外処理が必要)
    Works = list(map(lambda x: try_Work_get(x), arr))
    Works = [x for x in Works if x is not None]
    print(Works)
    return None if Works == [] else Works


def try_Work_get(id):
    try:
        return Work.objects.get(id=id)
    except Work.DoesNotExist:
        return None


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

    def __str__(self):
        return self.name
