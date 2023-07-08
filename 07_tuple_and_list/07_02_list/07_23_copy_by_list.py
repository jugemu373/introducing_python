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
