# dict()は2つの値のシーケンスを辞書に変換するためにも使える
lol = [['a', 'b'], ['c', 'd'], ['e', 'f']]
print(dict(lol))

# 2つのシーケンスを含むものなら何でも使える
# 2要素のタプルのリスト
lot = [('a', 'b'), ('c', 'd'), ('e' 'f')]
print(dict(lot))

# 2要素のリストのタプル
tol = (['a', 'b'], ['c', 'd'], ['e', 'f'])
print(dict(tol))

# 2要素の文字列のリスト
los = ['ab', 'cd', 'ef']
print(dict(los))

# 2文字の文字列のタプル
tos = ('ab', 'cd', 'ef')
print(dict(tos))
