# 名前付きタプル
"""
名前付きタプルはタプルのサブクラスで、位置([offset])だけでなく名前(.name)でも値にアクセスできる。

名前付きタプルはPythonが自動的に提供するデータ構造ではないので、モジュールをロードしてから使う必要がある。


名前付きタプルの長所をまとめると次のようになる。
・イミュータブルなオブジェクトのように見え、そのようにふるまう。
・オブジェクトよりも空間的、時間的に効率がよい。
・辞書スタイルの[]ではなく、ドット記法で属性にアクセスできる。
・辞書のキーとして使える。
"""
from collections import namedtuple


class Bill:
    def __init__(self, description):
        self.description = description


class Tail:
    def __init__(self, length):
        self.length = length


class Duck:
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail

    def about(self):
        print('This duck has a', self.bill.description,
              'bill and a', self.tail.length, 'tail')


Duck = namedtuple('Duck', 'bill tail')
duck = Duck('wide orange', 'long')
print(duck)
print(duck.bill)
print(duck.tail)

"名前付きタプルは辞書からも作ることができる"
parts = {'bill': 'wide orange', 'tail': 'long'}
duck2 = Duck(**parts)
print(duck2)

duck2 = Duck(bill='wide orange', tail='long')

"""
名前付きタプルはイミュータブルだが、1個以上のフィールドを交換した別の名前付きタプルを返すことはできる。
"""

duck3 = duck2._replace(tail='magnificent', bill='crushing')
print(duck3)


"""
duckは辞書としても定義することもできる
"""
duck_dict = {'bill': 'wide orange', 'tail': 'long'}
print(duck_dict)

"辞書にはフィールドを追加できる。"
duck_dict['color'] = 'green'
print(duck_dict)


"しかし、名前付きタプルには追加できない。"
duck.color = 'green'
print(duck)
