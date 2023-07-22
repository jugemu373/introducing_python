# match()による文字列の先頭の正確なマッチ
import re
source = 'Young Frankenstein'
m = re.match(r'You', source)        # matchはsourceの先頭にチェックする
if m:                               # matchはオブジェクトを返す。マッチした部分は次のようにして確かめる
    print(m.group())
m = re.match(r'^You', source)
if m:                               # パターンの先頭に^を付けても同じになる
    print(m.group())
m = re.match(r'Frank', source)
if m:
    print(m.group())
"""
match()は何も返しておらず、ifはprint文を実行しない。
Python3.8以降、いわゆるセイウチ演算子でこのコードを短くできるようになった。
"""
if m := re.match(r'Frank', source):
    print(m.group())
"search()を使ってソース文字列のどこかに'Frank'が含まれているかをチェックする。"
m = re.search(r'Frank', source)
if m:
    print(m.group())
"パターンを書き換えて、もう一度match()で先頭がマッチするかどうかをチェックする。"
m = re.match(r'.*Frank', source)
if m:                               # matchはオブジェクトを返す
    print(m.group())
"""
新しいパターンの意味を以下に示す。

・.は任意の1文字という意味。
・*は任意の個数の直前のものという意味である。.*全体では、任意の個数(0を含む)の任意の文字という意味。

match()は、.*Frankにマッチした文字列、'Young Frank'を返している。
"""
