'''
これは遺物. 現行はmodels.py のWorkに移植
from .models import Work

#import numpy as np  # numpyのimportの仕方分からず

num_of_works = Work.objects.all().count()
"""
avepointtmp = [[] for i in range(num_of_works)]
for i in range(num_of_works):
    work = Work.objects.get(id=i+1)
    avepointtmp[i] += list(map(lambda: x/work.num_of_data,
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

avepoint = np.array(avepointtmp)
stdpoint = np.std(statistics, axis=2)


def recommendsort(work_id):
    base = statistics-statistics[work_id-1]/stdpoint
    scores = np.sum(base, axis=1).tolist()
    for i in range(num_of_works):
        scores[i].append(i+1)
    scores.sort()
    return scores
"""
def recommendsort(work, n):
    # 作品ごとに評価項目の平均点を出す（評価データ数で割る）
    # 評価項目ごとに作品全体の標準偏差を出す
    # ある作品Aのスコアは評価項目ごとに
    # | Aの平均 - ベース作品の平均 |/標準偏差
    # の全評価項目総和
    # スコアは小さいほど近い作品. ベース作品のスコアは0
    avepoint = []
    squarepoint =[]
    sumpoint = [0 for i in range(num_of_works)]
    sumsqupoint = [0 for i in range(num_of_works)]
    for i in range(num_of_works):
        work = Work.objects.get(id=i+1)
        avepoint += list(map(lambda x: x/work.num_of_data,
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
        squarepoint += list(map(lambda x: x**2, avepoint[i*9:(i+1)*9]))
        sumpoint = list(map(lambda x, y: x+y, sumpoint, avepoint[i*9:(i+1)*9]))
        sumsqupoint = list(map(lambda x, y: x+y, sumsqupoint, squarepoint[i*9:(i+1)*9]))

    aveavepoint = list(map(lambda x: x/num_of_works, sumpoint))
    avesqupoint = list(map(lambda x: x/num_of_works, sumsqupoint))
    stdopint = list(map(lambda x, y: (x-y**2)**(-1/2),avesqupoint, aveavepoint))

    basework = avepoint[9*(work_id-1):9*work_id]
    scores = [[0, i+1]for i in range(num_of_works)]
    for i in range(num_of_works):
        scores[i][0] = sum(list(map(lambda x, y, z: abs(x-y)/z, avepoint[i*9:(i+1)*9], basework, stdopint)))

    scores.sort()
    tmp = []
    for work in scores:
        tmp.append(Work.objects.get(id=work[1]))  # idから作品に置き換え
    return tmp

"""
出力例（つもり）
scores=[
[0.0, 4], # 指定の作品そのもののため距離0
[0.4, 1],
[0.6, 6],
...
]
[指定の作品に対する距離, 作品ID(model:Workのものと一致)]
"""
'''