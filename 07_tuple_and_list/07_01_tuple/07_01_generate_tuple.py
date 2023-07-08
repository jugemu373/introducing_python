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
