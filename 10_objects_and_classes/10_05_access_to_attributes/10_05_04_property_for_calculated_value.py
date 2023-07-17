# 計算された値のためのプロパティ
"""
先は、オブジェクト内に格納されている単一の属性(hidden_name)を参照するために、nameプロパティを使っていた。
プロパティは、計算された値も消せる。
"""

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2 * self.radius
    

c = Circle(5)
print(c.radius)
print(c.diameter)


c.radius = 7
print(c.diameter)


"""
プロパティセッターを定義していなければ、外部からのプロパティを設定することはできない。
これは、読み出し専用のプロパティを作るときに便利である。
"""
print(c.diameter(20)) # AttributeErrorをスロー


"""
プロパティには、属性の直接アクセスよりも優れている大きなメリットがもう1つある。属性の定義を書き換えても、
クラス定義内のコードを書き換えるだけで済み、プロパティを呼び出しているコードには、手を付けなくて済むのである。
"""



