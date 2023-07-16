"""
属性は、クラスやオブジェクトの中の変数のことである。オブジェクトやクラスを作成している間、
あるいは、作成したあとに、それらに属性を与えることができる。属性はほかのオブジェクトなら何でもよい。
"""


class Cat():
    pass


a_cat = Cat()
print(a_cat)
another_cat = Cat()
print(another_cat)


a_cat.age = 3
a_cat.name = 'Mr. Fuzzybuttons'
a_cat.nemesis = another_cat

print(a_cat.age)
print(a_cat.name)
print(a_cat.nemesis)

a_cat.nemesis.name = 'Mr. Biggleworth'
print(a_cat.nemesis.name)


"""
単純なオブジェクトであっても、複数の属性を格納するために使える。リストや辞書のようなものではなく、
複数のオブジェクトを使えば、異なる値を格納することができる。

属性というとき、通常はオブジェクトの中の属性を意味するが、クラス属性もある。
"""
