# データ構造の振り返り
# ブール値、数値、文字列、タプル、リスト、辞書、集合
marxes = ['Groucho', 'Chico', 'Harpo']
pythons = ['Chapman', 'Cleese', 'Gilliam', 'Jones', 'Palin', 'Eric']
stooges = ['Moe', 'Curly', 'Larry']

# 個々のリストを要素とするタプルを作ることができる
tuple_of_lists = marxes, pythons, stooges
print(tuple_of_lists)

# 3つのリストを含むリストを作ることができる
list_of_lists = [marxes, pythons, stooges]
print(list_of_lists)

# リストの辞書の生成
dict_of_lists = {'Marxes': marxes, 'Pythons': pythons, 'Stooges': stooges}
print(dict_of_lists)


# 制限はデータ型自体にある
# 辞書のキーはイミュータブルでなければならない
# リスト、辞書、照合は他の辞書のキーにはなれないが、タプルはキーになれる
# 位置のGPS座標(緯度、経度、高度)をインデックスとして扱うことが可能
house = {
    (44.79, -93.14, 285): 'My House',
    (38.89, -77.03, 13): 'The White House'
}
print(house)
