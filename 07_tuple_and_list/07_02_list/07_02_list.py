# リストは、要素を順番に管理したいとき、順序と内容が変わる場合があるときに向いている
# リストは、ミュータブルである
# リストの内容は直接変更できる
# 新しい要素を追加したり、既存の要素を削除、置換したりできる
# リスト内では同じ値が複数回登場してもよい

import copy
sep = """
----------------------------------------
"""

# []による生成
# リストは、0個以上の要素をそれぞれカンマで区切り、全体を[]ブラケットで囲んで作る
empty_list = []
weekdays = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'saturday', 'sunday']
big_birds = ['emu', 'ostrich', 'cassowary']
first_names = ['Graham', 'John', 'Terry', 'Michael', 'Eric']
leap_years = [2000, 2004, 2008]
randomness = ['Punxsatawney', {"groundhog": "Phil"}, "Feb. 2"]

print(empty_list)
print(weekdays)
print(big_birds)
print(first_names)
print(leap_years)
print(randomness)

print(sep)


# list()による生成、変換
another_empty_list = list()
print(another_empty_list)

# list()は、他のイテラブル(タプル、文字列、集合、辞書)などをリストに変換することもできる
print(list('cat'))
a_tuple = ('ready', 'fire', 'aim')
print(list(a_tuple))

print(sep)


# split()による文字列からのリストの生成
talk_like_a_pirate_day = '9/19/2019'
print(talk_like_a_pirate_day.split('/'))
splitme = 'a/b//c/d///e'
print(splitme.split('/'))
print(splitme.split('//'))

print(sep)


# [offset]を使った要素を取り出し
# オフセットは、対象のリストの中で有効なものでなくてはならない
#
marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes[0])
print(marxes[1])
print(marxes[2])

print(sep)

print(marxes[-1])
print(marxes[-2])
print(marxes[-3])

print(sep)

# print(marxes[5])


# スライスによる要素の取り出し
# スライスを使うことによってリストのサブシーケンスを取り出すことができる
# リストのスライスもリストで返される
marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes[0:2])
print(sep)

# スライスは1以外のステップを指定できる
# 以下はリストを書き換えていない
print(marxes[::2])
print(marxes[::-2])
print(marxes[::-1])
print(sep)

# スライスは無効なインデックスを指定しても例外が発生しない。もっとも近い有効なインデックスに変身するか何も返さない
print(marxes[4:])
print(marxes[-6:])
print(marxes[-6:-2])
print(marxes[-6:-4])
print(sep)

# リストを直接逆順に書き換えるには、list.reverse()を使う
# revers()メソッドは、リストを書き換えるが値を返さない
marxes.reverse()
print(marxes)
print(sep)


# append()による末尾への要素の追加
# append()メソッドはリストの末尾に1つずつ要素を追加していく
marxes = ['Groucho', 'Chico', 'Harpo']
marxes.append('Zeppo')
print(marxes)
print(sep)


# insert()によるオフセットを指定した要素の追加
# insert()は、オフセットを指定し、その前に要素を追加する
# 末尾を超えるオフセットを指定した場合は、append()と同じ動きをとる
marxes = ['Groucho', 'Chico', 'Harpo']
marxes.insert(2, 'Gummo')
print(marxes)
marxes.insert(10, 'Zeppo')
print(marxes)
print(sep)

# *による全要素の繰り返し
print(["blah"] * 3)
print(sep)

# extend()または+=によるリストの結合
# extend()を使えば、他のリストを1つにまとめることができる
marxes = ['Groucho', 'Chico', 'Harpo']
others = ['Gummo', 'Zeppo']
marxes.extend(others)
print(marxes)
print(sep)

# + や +=でも連結することができる
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes += others
print(marxes)
print(sep)

# append()を使うとothersの要素を追加するのではなく、othersを1つの要素として追加する
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes.append(others)
print(marxes)
print(sep)


# offsetによる要素の書き換え
marxes = ['Groucho', 'Chico', 'Harpo']
marxes[2] = 'Wanda'
print(marxes)
print(sep)


# スライスによる要素の書き換え
numbers = [1, 3, 3, 4]
numbers[1:3] = [8, 9]
print(numbers)
print(sep)

# リストに代入する右辺の要素は、左辺のスライスと要素数が等しくなくても構わない
numbers = [1, 3, 3, 4]
numbers[1:3] = [7, 8, 9]
print(numbers)
print(sep)
numbers = [1, 3, 3, 4]
numbers[1:3] = []
print(numbers)

# 代入式の右辺はリストでなくてもよい
# Pythonのイテラブルなら、分割されてリスト要素に代入される
numbers = [1, 3, 3, 4]
numbers[1:3] = (98, 99, 100)
print(numbers)
print(sep)
numbers = [1, 3, 3, 4]
numbers[1:3] = 'what'
print(numbers)
print(sep)


# delによるオフセットを指定した要素の削除
marxes = ['Groucho', 'chico', 'Harpo', 'Gummo', 'Karl']
print(marxes[-1])
del marxes[-1]
print(marxes)
del marxes[1]
print(marxes)
print(sep)


# remove()による値を指定した要素の削除
# remove()は、値を指定して要素を削除する
marxes = ['Groucho', 'Chico', 'Harpo']
marxes.remove('Groucho')
print(marxes)
print(sep)


# pop()でオフセットを指定して要素を取り出し、削除する方法
# pop()はリストから要素を取り出し、同時にリストからその要素を削除できる
# オフセットを指定してpop()を呼び出すと、そのオフセットの要素が返される
# 引数を指定しない場合、デフォルトで-1が渡される
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print(marxes.pop())
print(marxes)
print(marxes.pop(1))
print(marxes)
print(sep)


# clear()による全ての要素の削除
work_quotes = ['Working_hard?', 'Quick question!', 'Number on priorities!']
print(work_quotes)
work_quotes.clear()
print(work_quotes)
print(sep)


# index()で要素の値から要素のオフセットを調べる
# リスト内に指定した値が複数ある場合、最初の要素のオフセットだけ返される
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print(marxes.index('Chico'))
simpsons = ['Lisa', 'Bart', 'Marge', 'Homer', 'Bart']
print(simpsons.index('Bart'))
print(sep)


# inによる値の有無のテスト
# 複数の位置に同じ値が格納されている場合がある、少なくても1か所に値があればinはTrueを返す
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
'Groucho' in marxes
'Bob' in marxes
words = ['a', 'deer', 'a', 'female', 'deer']
'deer' in words
print(sep)


# count()による値の個数の計算
marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes.count('Harpo'))
print(marxes.count('Bob'))
print(sep)
snl_skit = ['cheeseburger', 'cheeseburger', 'cheeseburger']
print(snl_skit.count('cheeseburger'))
print(sep)


# join()による文字列への変換
# join()メソッドは文字列のメソッドである
# join()はsplit()の逆である
marxes = ['Groucho', 'Chico', 'Harpo']
print(', '.join(marxes))
print(sep)
friends = ['Harry', 'Hermione', 'Ron']
separator = ' * '
joined = separator.join(friends)
print(joined)
separated = joined.split(separator)
print(separated)
separated == friends
print(sep)


# sort(), sorted()による要素の並べ替え
# sort()はリストのメソッドである。インプレースにリスト自体をソートする
# sorted()は組み込み関数である。ソートされたリストのコピーを返す
# リストの要素が数値なら、デフォルトで数値の昇順でソートする
# リストの要素が文字列ならアルファベット順でソートする
marxes = ['Groucho', 'Chico', 'Harpo']
sorted_marxes = sorted(marxes)
print(sorted_marxes)
print(marxes)
print(sep)
marxes.sort()
print(marxes)
print(sep)

# リストの要素が全て同じ型なら、sort()は正しく動作する
# 型が混ざっていてもいい場合がある
# 整数と浮動小数点数は、式の中ではPythonが自動的に変換を行う
numbers = [2, 1, 4.0, 3]
numbers.sort()
print(numbers)
print(sep)

# デフォルトのソート順は昇順だが、reverse=True引数を追加すると降順になる
numbers = [2, 1, 4.0, 3]
numbers.sort(reverse=True)
print(numbers)
print(sep)


# len()による長さの取得
# len()は、リスト内の要素数を返す
marxes = ['Groucho', 'Chico', 'Harpo']
print(len(marxes))
print(sep)


# =による代入
# 1つのリストを複数の変数に代入すると、その中の1つでリストを書き換えたときに、他のリストも書き換えられる
a = [1, 2, 3]
print(a)
b = a
print(b)
a[0] = 'surprise'
print(a)
print(b)
print(sep)
print(b)
b[0] = 'I hate surprises'
print(b)
print(a)
print(sep)


# copy(), list(), スライスによるコピー
# 以下の方法ではリストの値を独立の新しいリストにコピーできる
# リストのコピーメソッド
# list()関数
# リストスライス[:]
a = [1, 2, 3]
b = a.copy()
c = list(a)
d = a[:]
# b, c, d はa のコピーである。
# aが参照する[1, 2, 3]とは何の関係もない
a[0] = 'integer lists are boring'
print(a)
print(b)
print(c)
print(d)
print(sep)


# deepcopy()によるすべての要素のコピー
# copy()関数は、リストの要素がすべてのイミュータブルなら上手く機能する
# ミュータブルな値は参照である
# オリジナル化コピーのどちらかに変更を加えると、両方に変更が反映される
a = [1, 2, [8, 9]]
b = a.copy()
c = list(a)
d = a[:]
print(a)
print(b)
print(c)
print(d)
print(sep)

# shallow copy(値がミュータブルかどうかを判断せず、深さ1で全てのものコピーするだけ)の例を示す
a[2][1] = 10
print(a)
print(b)
print(c)
print(d)
print(sep)

# shallow copyでなないコピーをするためには、deepcopy()を使う
# deepcopy()なら、深くネストされたリスト、辞書、その他のミュータブルオブジェクトを完全にコピーできる
a = [1, 2, [8, 9]]
b = copy.deepcopy(a)
print(a)
print(b)
a[2][1] = 10
print(a)
print(b)
print(sep)


# リストの比較
# リストは、==, < などの比較演算子で直接比較できる
# 両方のリストをたどり、同じオフセットの要素を比較する
# リストaがリストよりも短く、ある要素がすべて等しければaはbよりも「小さい」と判断される
a = [7, 2]
b = [7, 2, 9]
a == b
a <= b
a < b
print(sep)


# forとinによる反復処理
cheeses = ['brie', 'gjetost', 'havarti']
for cheese in cheeses:
    print(cheese)
print(sep)

# breakとcontinueを使ったfor文
cheeses = ['brie', 'gjetost', 'havarti']
for cheese in cheeses:
    if cheese.startswith('g'):
        print("I won't eat anything that starts with 'x'")
        break
    else:
        print(cheese)
print(sep)

# オプションelseも使うことができる
cheeses = ['brie', 'gjetost', 'havarti']
for cheese in cheeses:
    if cheese.startswith('g'):
        print("I won't eat anything that starts with 'x'")
        break
    else:
        print(cheese)
else:
    print("Didn't find anything that started with 'x")
print(sep)

# 最初のforが実行されない場合も、制御はelseに移る
cheeses = []
for cheese in cheeses:
    print('This shop has some lively', cheese)
    break
else:   # breakされなければチーズはない
    print('This is not much of a cheese shop, is it?')
print(sep)


# zip()による複数のシーケンスの反復処理
# zip()を使えば、複数のシーケンスを並行して反復処理できる
# zip()は、もっとも短いシーケンスの用を処理し尽くしたときに止まる
days = ['Monday', 'Tuesday', 'wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ise cream', 'pie', 'pudding']
for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day, ":drink", drink, "- eat", fruit, "- enjoy", dessert)
print(sep)

# 複数のシーケンスをたどって、オフセットが共通する要素からタプルを作ることができる
english = 'Monday', 'Tuesday', 'Wednesday'
french = 'lundi', 'mardi', 'mercredi'
print(list(zip(english, french)))
# zip()の結果を直接dict()に渡すと、英仏辞書ができあがる
print(dict(zip(english, french)))
print(sep)


# リスト内包表記による作成
# リストは、リスト内法表記でも生成できる
# 1から5までの整数のリストは、次のように一度に1つずつ要素を追加すれば作れる
number_list = []
number_list.append(1)
number_list.append(2)
number_list.append(3)
number_list.append(4)
number_list.append(5)
print(number_list)

# 反復子とrange()で生成
number_list = []
for number in range(1, 6):
    number_list.append(number)
print(number_list)

# range()の出力を直接リストに変換しても作れる
number_list = list(range(1, 6))
print(number_list)
print(sep)

# パフォーマンスを求める場合、リスト内法表記を使うケースがある
# 構文: [expression for item in iterable]
number_list = [number for number in range(1, 6)]
print(number_list)
number_list = [number -1 for number in range(1, 6)]
print(number_list)
print(sep)

# リスト内法表記には条件式も追加できる
# 構文: [expression for item in iterable if condition]
a_list = [number for number in range(1, 6) if number % 2 == 1]
print(a_list)
a_list = []
for number in range(1, 6):
    if number % 2 == 1:
        a_list.append(number)
print(a_list)
print(sep)

# リスト内法表記はネストにできる
rows = range(1, 4)
cols = range(1, 3)
for row in rows:
    for col in cols:
        print(row, col)

rows = range(1, 4)
cols = range(1, 3)
cells = [(row, col) for row in rows for col in cols]
for cell in cells:
    print(cell)

# タプルのアンパックを使って、cellsリストを反復処理しながらタプルからrow, colの値を抜き出すことができる
for row, col in cells:
    print(row, col)
print(sep)


# リストのリスト
small_birds = ['hummingbird', 'finch']
extinct_birds = ['dodo', 'passenger pigeon', 'Norwegian Blue']
carol_birds = [3, 'French hens', 2, 'turtledoves']
all_birds = [small_birds, extinct_birds, carol_birds]
print(all_birds)
print(all_birds[0])
print(all_birds[1])
print(all_birds[1][0])
