
#これは遺物. 現行はmodels.py のWorkに移植
#今なら作れる気がする
from .models import Work

#import numpy as np
# numpyのimportの仕方分からず

def get_works():
    return Work.objects.all()

def get_num_of_works():
    return get_works().count()

def get_std():
    """各評価項目の標準偏差を出す。返り値はリスト型評価項目の順序はmodel参照"""
    num = get_num_of_works()
    sumpoint = [0 for i in range(num)]
    sumsqupoint = [0 for i in range(num)]
    for work in get_works():
        sumpoint = list(map(lambda x, y: x + y, sumpoint, work.get_average()))
        sumsqupoint = list(map(lambda x, y: x + y ** 2, sumsqupoint, work.get_average()))
    avepoint = list(map(lambda x: x / num, sumpoint))
    avesqupoint = list(map(lambda x: x / num, sumsqupoint))
    stdopint = list(map(lambda x, y: (x - y ** 2) ** (-1 / 2), avesqupoint, avepoint))
    return stdopint


def recommendsort(object, n):
    """
    作品Aのスコアは　|Aの平均 - ベース作品の平均|/標準偏差　の全評価項目総和
    スコアは小さいほどおすすめ作品であり、ベース作品がWorkオブジェクトならばスコア0でindex0がベース作品になる。
    AddedWorkオブジェクトをベース作品に指定した場合index0はベース作品ではない。
    nは返り値の作品数。ここは返り値をもらってからスライスする仕様に換えても何ら問題ないので使いやすいようにするといい。
    """
    try:
        ###Workの場合
        basepoint=object.get_average()
    except:
        ###AddedWorkの場合
        basepoint=[object.joy,object.anger,object.sadness,object.fun,object.tech_constitution,object.tech_story,object.tech_character,object.tech_speech,object.tech_picture]
    scores = []
    for work in get_works():
        scores += [
            [sum(list(map(lambda x, y, z: abs(x - y) / z, work.get_average(), basepoint, get_std()))),
             work]]
    scores.sort()
    works = []
    for score, work in scores:
        works.append(work)
        if(len(works)>=n):break
    return works
