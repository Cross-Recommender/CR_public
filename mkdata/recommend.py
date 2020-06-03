
#これは遺物. 現行はmodels.py のWorkに移植
#今なら作れる気がする
from .models import Work, AddedWork, mkbaseWorks

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
                 work.id]]
    scores.sort(key=lambda x: x[0])
    works = []
    for score, workid in scores:
        works.append(workid)
        if len(works) >= n:
            break
    return works


def recommendselect(user):

    OrderedWork = mkbaseWorks(user.work_like)
    #print(user.work_like[:10])
    #print(OrderedWork)
    print(OrderedWork is None)
    if OrderedWork is None:
        OrderedWork = AddedWork.objects.filter(userid=user.id).order_by('-like')[:5].order_by('?')
        if OrderedWork.count() == 0:
            return None

    works = []
    num = 0
    for work in OrderedWork:
        # print(len(works))#なぜか作品が6つ以上表示された時のバグ確認用
        cand_works = recommendsort(work, 5)
        # print(OrderedWork[num], cand_works)
        for i in range(4):
            # print((cand_works[i] in works) == False,user.work_like[cand_works[i]-1] == '0')
            if (cand_works[i] in works) is False and user.work_like[cand_works[i] - 1] == '0':
                ###work_readは一時的な記録に過ぎないため, ユーザが読んだかどうかの判定は
                ###user.work_like[cand_works[i]-1] == '0'で行う
                works.append(cand_works[i])
            if len(works) >= 5:
                break
        if len(works) >= 5:
            break
        num += 1
        if num == 4:
            break
    user.work_recommend = works
    user.save()


    return
