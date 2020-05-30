# -*- coding: utf-8 -*-
import json
import csv

### 使い方
# with open (input)にinputファイル名を入れる
# with open (output)にoutputファイル名を入れる
# inputファイルは前処理が必要
# 前処理1. utf-8で保存
# 前処理2. ヘッダはいらない削除
# 今後関数化して引数にファイル名を入れられるようにする予定
# エラー処理も書いてないので逐次アップデート予定
 
json_list = []
keys = ('name','num_of_data','like','joy','anger','sadness','fun','tech_constitution','tech_story','tech_character','tech_speech','tech_picture')

# CSV ファイルの読み込み
with open('(input).csv', 'r', encoding='utf-8') as f:
    for i,row in enumerate(csv.DictReader(f, keys),1):
        name = row.pop('name')
        for obj in row.items():
            val = float(obj[1])
            row[obj[0]] = int(val)
        #print(row)
        row.update(name=name)
        row.move_to_end('name',False)
        #print(row)
        work={"model": "mkdata.work", "pk": i, "fields": row}
        json_list.append(work)

# JSON ファイルへの書き込み
with open('(output).json', 'w',encoding='utf-8') as f:
    #print(json_list)
    json.dump(json_list, f, ensure_ascii=False)