# 書き換えられない集合を生成するときは、イテラブル引数を指定してfrozenset()を呼び出す
print(frozenset([3, 2, 1]))
print(frozenset(set({1, 2, 3})))
print(frozenset({3, 2, 1}))
print(frozenset((2, 3, 2)))

fs = frozenset([3, 2, 1])
print(fs)
fs.add(4)
