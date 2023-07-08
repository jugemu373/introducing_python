# deepcopy()によるすべての要素のコピー
# copy()関数は、リストの要素がすべてのイミュータブルなら上手く機能する
# ミュータブルな値は参照である
# オリジナル化コピーのどちらかに変更を加えると、両方に変更が反映される

import copy

a = [1, 2, [8, 9]]
b = a.copy()
c = list(a)
d = a[:]
print(a)
print(b)
print(c)
print(d)

# shallow copy(値がミュータブルかどうかを判断せず、深さ1で全てのものコピーするだけ)の例を示す
a[2][1] = 10
print(a)
print(b)
print(c)
print(d)

# shallow copyでなないコピーをするためには、deepcopy()を使う
# deepcopy()なら、深くネストされたリスト、辞書、その他のミュータブルオブジェクトを完全にコピーできる
a = [1, 2, [8, 9]]
b = copy.deepcopy(a)
print(a)
print(b)
a[2][1] = 10
print(a)
print(b)
