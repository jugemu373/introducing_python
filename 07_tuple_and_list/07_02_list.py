# リストは、要素を順番に管理したいとき、順序と内容が変わる場合があるときに向いている
# リストは、ミュータブルである
# リストの内容は直接変更できる
# 新しい要素を追加したり、既存の要素を削除、置換したりできる
# リスト内では同じ値が複数回登場してもよい

sep = """
----------------------------------------
"""

# []による生成
# リストは、0個以上の要素をそれぞれカンマで区切り、全体を[]ブラケットで囲んで作る
empty_list = []
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'saturday', 'sunday']
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

# スライスは1以外のステップを指定できる
# 以下はリストを書き換えていない
print(marxes[::2])
print(marxes[::-2])
print(marxes[::-1])

# スライスは無効なインデックスを指定しても例外が発生しない。もっとも近い有効なインデックスに変身するか何も返さない
print(marxes[4:])
print(marxes[-6:])
print(marxes[-6:-2])
print(marxes[-6:-4])

# リストを直接逆順に書き換えるには、list.reverse()を使う
# revers()メソッドは、リストを書き換えるが値を返さない
marxes.reverse()
print(marxes)


# append()による末尾への要素の追加
# append()メソッドはリストの末尾に1つずつ要素を追加していく
marxes = ['Groucho', 'Chico', 'Harpo']
marxes.append('Zeppo')
print(marxes)


# insert()によるオフセットを指定した要素の追加
# insert()は、オフセットを指定し、その前に要素を追加する
# 末尾を超えるオフセットを指定した場合は、append()と同じ動きをとる
marxes = ['Groucho', 'Chico', 'Harpo']
marxes.insert(2, 'Gummo')
print(marxes)
marxes.insert(10, 'Zeppo')
print(marxes)


# *による全要素の繰り返し
print(["blah"] * 3)


# extend()または+=によるリストの結合
# extend()を使えば、他のリストを1つにまとめることができる
marxes = ['Groucho', 'Chico', 'Harpo']
others = ['Gummo', 'Zeppo']
marxes.extend(others)
print(marxes)

# + や +=でも連結することができる
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes += others
print(marxes)

# append()を使うとothersの要素を追加するのではなく、othersを1つの要素として追加する
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes.append(others)
print(marxes)


# offsetによる要素の書き換え
