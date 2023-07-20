# itertoolsによるコード構造の反復処理
"""
itertools()には、特別な目的を持つイテレータ関数が含まれている。これらは、for ... in ループ内で呼び出されると、一度に1個の要素を返し、
呼び出しの間も自分の状態を覚えている。
"""
import itertools


"chain()は、引数全体が1つのイテラブルであるかのように扱い、その中の要素を反復処理する。"
for item in itertools.chain([1, 2], ['a', 'b']):
    print(item)

"cycle()は無限イテレータで、引数から循環的に要素を返す。"
for item in itertools.cycle([1, 2]):
    print(item)

"accumulate()は、それまでの要素を1つにまとめた値を計算する。デフォルトでは和を計算する。"
for item in itertools.accumulate([1, 2, 3, 4]):
    print(item)

"""
accumulate()は、第2引数として関数を受付、この引数が加算の代わりに使われる。
この関数は、2個の引数を受け付け、1この結果を返すものでなければならない。
"""
def multiply(a, b):
    return a * b


for item in itertools.accumulate([1, 2, 3, 4], multiply):
    print(item)


"""
itertoolsモジュールは、これら以外にも多くの関数を定義している。特に順列、組み合わせの関数は、必要なときに時間の節約になる。
"""
