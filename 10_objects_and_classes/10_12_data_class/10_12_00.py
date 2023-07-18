# データクラス
"""
多くの人々は主としてデータを格納するため(属性として)にオブジェクトを作るが、それほど動作(メソッド)を定義するわけではない。
オブジェクトに関わるデータストアとして名前付きタプルを見たところだが、Python3.7からはデータクラスも使えるようになった。
属性(name)を1つだけ持つ旧来のオブジェクトは次のようにして作る。
"""
from dataclasses import dataclass


class TeenyClass:
    def __init__(self, name):
        self.name = name


teeny = TeenyClass('itsy')
print(teeny.name)


"データクラスを使って同じことをすると、少しコードが違ったものになる。"


@dataclass
class TeenyDataClass:
    name: str


teeny = TeenyDataClass('bitsy')
print(teeny.name)


"""
デコレータ@dataclassが必要になることに加え、color: strやcolor: str = "red"のようにname: typeやname: type = valという
形式の変数アノテーションを使って属性を定義するようになる。typeは、strやintといった組み込み型だけでなく、自作のクラスでもよい。

データクラスオブジェクトを作るときには、クラスで定義された順序で実引数を渡していくか、名前付き引数を意使う。
"""


@dataclass
class AnimalClass:
    name: str
    habitat: str
    teeth: int = 0


snowman = AnimalClass('yeti', 'Himalayas', 46)
duck = AnimalClass(habitat='lake', name='duck')
print(snowman)
print(duck)

"""
AnimalClassは、teeth属性についてデフォルト値を指定しているので、duckを作るときにはteethを指定する必要はない。
"""
print(duck.habitat)
print(snowman.teeth)
