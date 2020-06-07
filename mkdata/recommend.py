from .models import Work, AddedWork, try_Work_get
import random

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

def user_standardize(obj):
    ### user.work_evaluationの情報から, 評価した作品に対して, そのユーザの各項目の平均値, 標準偏差を出す

    info = [[0,0,0] for _ in range(20)]###[その項目の評価数, その項目の評価点合計, その項目の評価点の2乗の合計]
    for i, workid in enumerate(obj.work_evaluated):
        if int(obj.work_read[workid-1]) >= 3:
            for j, val in enumerate(obj.work_evaluation[i]):###0は'like'なので計算の必要なし
                info[j][0] += 1
                info[j][1] += val
                info[j][2] += val**2

    data = [[0,0] for _ in range(20)]###[その項目の平均評価, その項目の標準偏差]

    for i in range(1,20):###0は'like'なので計算の必要なし
        if info[i][0] == 0:
            pass
        else:
            data[i][0] = info[i][1]/info[i][0]
            data[i][1] = info[i][2]/info[i][0] - (info[i][1]/info[i][0])**2
            if obj.evaluation_avg is None:
                obj.evaluation_avg = [0]*20
                obj.evaluation_std = [0]*20
            #print(obj.evaluation_avg)
            obj.evaluation_avg[i] = data[i][0]
            obj.evaluation_std[i] = data[i][1]

    obj.save()

    ###標準化したユーザーの評価値を各モデルに加算
    for i, workid in enumerate(obj.work_evaluated):
        if int(obj.work_read[workid-1]) >= 3:
            work = Work.objects.get(id=workid)

            ###今までの回答有無に関わらずvoteで今までの回答をリセットしたので, ここまでたどり着いたらまた1増やす
            work.num_of_data += 1

            ###work.likeは標準化せずそのまま足す
            work.like += obj.work_evaluation[i][0]

            for j, val in enumerate(obj.work_evaluation[i]):###0は'like'なので計算の必要なし
                if val == 0:###その作品のジャンルには含まれない指標
                    continue

                ###標準化した値でwork_evaluationを上書き
                #work_evaluationは正規化以前の値をそのまま入れておく
                #2回目以降のstandarizeで壊れるため
                if data[j][1] != 0:
                    val = (val - data[j][0]) / data[j][1]
                else:
                    val = data[j][0]

                ###Workモデルの書き換え
                if j == 1:
                    work.joy += val
                elif j == 2:
                    work.anger += val
                elif j == 3:
                    work.sadness += val
                elif j == 4:
                    work.fun += val
                elif j == 5:
                    work.tech_constitution += val
                elif j == 6:
                    work.tech_story += val
                elif j == 7:
                    work.tech_character += val
                elif j == 8:
                    work.tech_speech += val
                elif j == 9:
                    work.tech_picture += val
                elif j == 10:
                    work.mov_tech_audio += val
                elif j == 11:
                    work.mov_tech_acting += val

            work.save()
    obj.save()



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
    if basepoint is None:
        return None
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
    #print(not OrderedWork)
    OrderedAddedWork = mkbaseAddedWorks(user.id)
    #print(OrderedAddedWork)
    #print(not OrderedAddedWork)
    OrderedWork += OrderedAddedWork
    if not OrderedWork:  #これで空っぽ判定になるらしい
        user.work_recommend = None
        user.save()
        return

    works = []
    num = 0

    ###recommend_sortを行う前に, userのデータを標準化, workモデルに反映
    user_standardize(user)

    for work in OrderedWork:
        # print(len(works))#なぜか作品が6つ以上表示された時のバグ確認用
        cand_works = recommendsort(work, 5)
        if cand_works is None:
            continue
        # print(OrderedWork[num], cand_works)
        for i in range(4):
            # print((cand_works[i] in works) == False,user.work_like[cand_works[i]-1] == '0')
            if (cand_works[i] in works) is False and user.work_read[cand_works[i] - 1] < '2':
                ###ユーザが読んだかどうかの判定は
                ###user.work_read[cand_works[i]-1] < '2'で行う
                works.append(cand_works[i])
            if len(works) >= 5:
                break
        if len(works) >= 5:
            break
        num += 1
        if num == 4:
            break
    if not works:
        works = [0]*5
    user.work_recommend = works
    user.save()
    return

def mkbaseWorks(string):
    """
    work_like をもとにユーザーの高評価作品順に並んだ　works　を返す
    評価点が同じ作品の順序はランダムに決まる
    この関数を呼び出すたびに順番は変わる
    """
    ###Workデータベースの最大IDはobjects.all().count()で得られない
    arr = list(map(lambda x: int(x)+random.random(), list(string[:Work.objects.all().order_by("-id")[0].id])))
    arr = list(enumerate(arr, 1))
    arr.sort(key=lambda x: x[1], reverse=True)
    arr = [x for x in arr if x[1] >= 1]
    arr = list(map(lambda x: x[0], arr))
    #print(arr)
    ###オブジェクト削除によりオブジェクトがない場合があるので例外処理
    Works = list(map(lambda x: try_Work_get(x), arr))
    Works = [x for x in Works if x is not None]
    #print(Works)
    return Works


def mkbaseAddedWorks(userid):
    AddedWorks = list(map(lambda x: [x, x.like + random.random()], AddedWork.objects.filter(userid=userid)))
    AddedWorks.sort(key=lambda x: x[1], reverse=True)
    AddedWorks = list(map(lambda x: x[0], AddedWorks))
    return AddedWorks
