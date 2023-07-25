# scandir()によるディレクトリ一覧の作成
"ディレクトリを作り、ファイルも作成する。"
import os
os.mkdir('poems')

"ディレクトリに含まれるもののリストを取得する。"
with os.scandir("poems") as it:
    entries = [entry.name for entry in it]

print(entries)

"サブディレクトリを作成"
os.mkdir('poems/mcintyre')
with os.scandir('poems') as it:
    entries = [entry.name for entry in it]

print(entries)

"このサブディレクトリにファイルを作る。"
fout = open('poems/mcintyre/the_good_man.txt', 'w')
fout.write("""Cheerful and happy was hit mood,
           He to the poor was kind and good,
           And he oft' times did find them food,
           Also supplies of coal nd wood,
           He never spake a word was rude,
           And cheer'd those did o7er sorrows brood,
           He passed away not understood,
           Because no poet in his lays
           Had penned a sonnet in his praise,
           'Tis sad, but such is world's ways.
           """)
fout.close()

with os.scandir('poems/mcintyre') as it:
    entries = [entry.name for entry in it]

print(entries)
