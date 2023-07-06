# タプルはイミュータブルである


# 空のタプルの生成
empty_tuple = ()
print(empty_tuple)


# 1個以上の要素を持つタプルは、個々の要素をカンマで区切る
# 要素が1個以上のタプルにも末尾にカンマを付けて作る
one_marx = 'Groucho',
print(one_marx)

# 要素を()で囲んでも同じタプルを作れる
one_marx = ('Groucho',)
print(one_marx)

# ()内に1つのものしか含まれておらず、カンマがなければタプルではないただのオブジェクトになる
one_marx = ('Groucho')
print(one_marx)
print(type(one_marx))

# 要素が複数ある場合には、すべての要素の後ろにカンマをつける(最後の要素の後ろのカンマは省略可)
marx_tuple = 'Groucho', 'Chico', 'Harpo'
print(marx_tuple)

# Pythonはタプルをエコー表示するときに()をつけて返す
# タプルを定義するときには()が不要な場合が多いが、()を使った方が安全であり可読性が上がる
marx_tuple = ('Groucho', 'Chico', 'Harpo')
print(marx_tuple)

# カンマに別の用途がある場合には、()が必要
# 1要素タプルの初期化、代入では末尾にカンマを付けるだけでよいが、この形のもを関数への引数として渡すことはできない
one_marx = 'Groucho',
print(type(one_marx))
print(type('Groucho',))
print(type(('Groucho',)))

# タプルは一度に複数の引数を代入できる
# タプルのアンパック
marx_tuple = ('Groucho', 'Chico', 'Harpo')
a, b, c = marx_tuple
print(a)
print(b)
print(c)

# タプルを使えば、一時変数を使わずに1つの文で値を交換できる
password = 'swordfish'
icecream = 'tuttifrutti'
password, icecream = icecream, password
print(password)
print(icecream)


# tuple()によるタプルの生成
# tuple()を使えば、他のデータ型のものからタプルを作れる
marx_list = ['Groucho', 'Chico', 'Harpo']
print(tuple(marx_list))


# +演算子によるタプルの連結
print(('Groucho',) + ('Chico', 'Harpo'))


# *演算子によるタプルの繰り返し
print(('yada') * 3)


# タプルの比較
# リストの比較と似ている
a = (7, 2)
b = (7, 2, 9)
print(a == b)
print(a <= b)
print(a < b)


# forとinによる反復処理
words = ('fresh', 'out', 'of', 'ideas')
for word in words:
    print(word)


# タプルの書き換え
# タプルを書き換えることはできない
# タプルは文字列同様にイミュータブルであり、既存のタプルを書き換えることはできない
# 文字列と同様に既存のタプルを連結して新しいタプルを作れる
t1 = ('Fee', 'Fie', 'Foe')
t2 = ('Flop',)
print(t1 + t2)

# 以下の方法でタプルを書き換えることができる
t1 += t2
print(t1)

# 94行目と88行目のt1は同じタプルではない
# 93行目の時点で新しい変数を生成し、その変数にt1という名前をつけている
