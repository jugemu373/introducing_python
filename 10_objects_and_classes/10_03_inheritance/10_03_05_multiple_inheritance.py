# 多重継承
"""
オブジェクトは複数の親クラスを継承することができる。

クラスが自分では持っていないメソッドや属性を参照すると、Pythonはすべての親クラスを覗く。Pythonの継承はメソッド解決順序によって決まる。
個々のPythonクラスは、そのクラスのオブジェクトがメソッドや属性を探すときに参照するクラスのリストを返す特別なメソッドmro()を持つ。
また、それらのクラスのタプルを格納する__mro__という属性もある。

厳密にはC3線形化アルゴリズムと呼ばれる手法でメソッド解決順序を決定している。
"""


class Animal:
    def says(self):
        return 'I speak!'


class Horse(Animal):
    def says(self):
        return 'Neigh!'


class Donkey(Animal):
    def says(self):
        return 'Hee-haw!'


class Mule(Donkey, Horse):
    pass


class Hinny(Horse, Donkey):
    pass


"""
Muleのメソッドや属性を探すとき、Pythonは順に次のものを見ていく

1. オブジェクト自体(Mule型)
2. オブジェクトのクラス(Mule)
3. オブジェクトの第1親クラス(Donkey)
4. オブジェクトの第2親クラス(Horse)
5. オブジェクトの祖父母クラス(Animal)
"""

Mule.mro()
Hinny.mro()

mule = Mule()
hinny = Hinny()
print(mule.says())
print(hinny.says())
