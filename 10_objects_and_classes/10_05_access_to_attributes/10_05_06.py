# クラスの属性とインスタンスの属性
"""
クラスには、属性を追加できる。このような属性は、クラスから作られたインスタンスにそのまま受け継がれる。
"""


class Fruit:
    color = 'red'


blueberry = Fruit()
print(Fruit.color)
print(blueberry.color)

"しかし、インスタンスの属性の値を変更しても、クラスの属性に影響は及ばない"
blueberry.color = 'blue'
print(blueberry.color)
print(Fruit.color)

"あとでクラス属性を変更しても、既存のインスタンスには影響を与えない。"
Fruit.color = 'orange'
print(Fruit.color)
print(blueberry.color)

"しかし、新しいオブジェクトには影響を及ぼす。"
new_fruit = Fruit()
print(new_fruit.color)
