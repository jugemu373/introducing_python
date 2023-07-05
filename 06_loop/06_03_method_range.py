# range()は指定した範囲の数値のシーケンスを返すことができる
# 構文: range(start, stop, step)
# デフォルト引数: start = 0, stop = 1, step = 1
# 引数stepは省略可。負数を指定することで逆順することも可
# 必須引数はstopのみ
# 戻り値: イテラブルなオブジェクト
# 戻り値は反復処理に使うか、listなどのシーケンスに変換しなければならい
for x in range(0, 3):
    print(x)

print(list(range(0, 3)))

for x in range(2, -1, -1):
    print(x)

print(list(range(2, -1, -1)))
