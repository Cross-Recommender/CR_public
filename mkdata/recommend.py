
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
        work_ave = work.get_average()
        if work_ave is None:
            num -= 1
        else:
            sumpoint = list(map(lambda x, y: x + y, sumpoint, work_ave))
            sumsqupoint = list(map(lambda x, y: x + y ** 2, sumsqupoint, work_ave))
    if num == 0:
        print("No Works are registered.")
    avepoint = list(map(lambda x: x / num, sumpoint))
    avesqupoint = list(map(lambda x: x / num, sumsqupoint))
    stdopint = list(map(lambda x, y: (x - y ** 2) ** (-1 / 2), avesqupoint, avepoint))
    return stdopint


def recommendsort(obj, n):
    """
    作品Aのスコアは　|Aの平均 - ベース作品の平均|/標準偏差　の全評価項目総和
    スコアは小さいほどおすすめ作品であり、ベース作品がWorkオブジェクトならばスコア0でindex0がベース作品になる。
    AddedWorkオブジェクトをベース作品に指定した場合index0はベース作品ではない。
    nは返り値の作品数。ここは返り値をもらってからスライスする仕様に換えても何ら問題ないので使いやすいようにするといい。
    """
    try:
        ###Workの場合
        basepoint = obj.get_average()
    except AttributeError:
        ###AddedWorkの場合
        basepoint=[obj.joy,obj.anger,obj.sadness,obj.fun,obj.tech_constitution,obj.tech_story,obj.tech_character,obj.tech_speech,obj.tech_picture]
    scores = []
    for work in get_works():
        if work.num_of_data != 0:
            scores += [
                [sum(list(map(lambda x, y, z: abs(x - y) / z, work.get_average(), basepoint, get_std()))),
                 work]]
    scores.sort(key=lambda x: x[0])
    works = []
    for score, work in scores:
        works.append(work)
        if len(works) >= n:
            break
    return works
