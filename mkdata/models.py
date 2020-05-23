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


    # 作品ごとに評価項目の平均点を出す（評価データ数で割る）
    # 評価項目ごとに作品全体の標準偏差を出す
    # ある作品Aのスコアは評価項目ごとに
    # | Aの平均 - ベース作品の平均 |/標準偏差
    # の全評価項目総和
    # スコアは小さいほど近い作品. ベース作品のスコアは0
    def recommendsort(self, n):
        num_of_works = Work.objects.count()
        works = Work.objects.all()
        work_ids=[]
        avepoint = []
        squarepoint = []
        sumpoint = [0 for i in range(num_of_works)]
        sumsqupoint = [0 for i in range(num_of_works)]
        i = 0
        for work in works:
            avepoint += list(map(lambda x: x / work.num_of_data,
                                 [work.joy,
                                  work.anger,
                                  work.sadness,
                                  work.fun,
                                  work.tech_constitution,
                                  work.tech_story,
                                  work.tech_character,
                                  work.tech_speech,
                                  work.tech_picture
                                  ]))
            squarepoint += list(map(lambda x: x ** 2, avepoint[i * 9:(i + 1) * 9]))
            sumpoint = list(map(lambda x, y: x + y, sumpoint, avepoint[i * 9:(i + 1) * 9]))
            sumsqupoint = list(map(lambda x, y: x + y, sumsqupoint, squarepoint[i * 9:(i + 1) * 9]))
            i += 1
            work_ids.append(work.id)

        aveavepoint = list(map(lambda x: x / num_of_works, sumpoint))
        avesqupoint = list(map(lambda x: x / num_of_works, sumsqupoint))
        stdopint = list(map(lambda x, y: (x - y ** 2) ** (-1 / 2), avesqupoint, aveavepoint))
        avebasework = list(map(lambda x: x / self.num_of_data,
                                 [self.joy,
                                  self.anger,
                                  self.sadness,
                                  self.fun,
                                  self.tech_constitution,
                                  self.tech_story,
                                  self.tech_character,
                                  self.tech_speech,
                                  self.tech_picture
                                  ]))

        scores = []
        for i in range(num_of_works):
            scores += [[sum(list(map(lambda x, y, z: abs(x - y) / z, avepoint[i * 9:(i + 1) * 9], avebasework, stdopint))),
                       work_ids[i]]]

        scores.sort()
        works = []
        for i in range(1, min(n, num_of_works)):
            works.append(Work.objects.get(id=scores[i][1]))
        return works

# work_like を元にユーザーの高評価作品順に並んだ　works　を返す
# 都合がいいので仮置き　cms/views.py で使用
def mkbaseWorks(string):
    arr = list(map(lambda x: int(x), list(string[:Work.objects.count()])))
    arr = list(enumerate(arr, 1))
    arr.sort(key=lambda x: x[1])
    arr = list(map(lambda x: x[0], arr))
    Works = list(map(lambda x: Work.objects.get(id=x), arr))
    return Works