"""
作成時にオブジェクトの属性に値を代入したい場合には、Pythonのオブジェクト初期化の為の特殊メソッド__init__()が必要になる。
"""
# class Cat()
#     def __init__(self):
#         pass


"""
Pythonクラス定義に含まれているものである。__init__()とselfは奇妙に思えるだう。__init__()は、クラス定義から個々のオブジェクトを
作るときにそれを初期化するメソッドに付けられた特殊名である。self引数は、作られた個別のオブジェクト自体を参照することを示す。

クラス定義で__init__()を定義するときには、第1引数はselfでなければならない。selfはPythonの予約語ではないが、一般にこの目的で使われる。
selfを使っておけば、あとでこのコードを読む人は、それがどういう意味なのかを推測しなくて済む。
"""
class Cat():
    def __init__(self, name):
        self.name = name


furball = Cat('Grumpy')
"""
このコードは以下のことを行う。

・Catクラスの定義を探し出す。
・メモリ内に新しいオブジェクトのインスタンスを生成する
・メモリ内に新しく作ったオブジェクト、nameとしてもう1つの引数('Grumpy')を渡して、オブジェクトの__init__()メソッドを呼び出す。
・nameの値をオブジェクトに格納する。
・その新しいオブジェクトを返す。
・オブジェクトにfurballという名前を与える。
"""


"""
このオブジェクトは、リスト、タプル、辞書、集合の要素として扱うことができる。関数に引数を渡したり、関数から結果として返したりすることもできる。

渡されたnameの値は、属性としてオブジェクトとともに保存される。属性は直接読み書きができる。
"""
print('Our Latest addition:', furball.name)

"""
Catクラス内部では、name属性にはself.nameという形でアクセスする。実際のオブジェクトを作り、それをfurballのような変数に代入した場合、
オブジェクトの外からはfurball.nameと呼ぶ。

すべてのクラス定義が__init__()を持たなければならないわけではない。
__init__()は、同じクラスから作られたほかのオブジェクトからこのオブジェクトを区別するために必要な処理をするために使われる。
これは、他の言語で「コンストラクタ」と呼んでいるものとは異なる。Pythonは__init__()を呼び出す前に既にオブジェクトを構築している。
__init__()は、イニシャライザ(初期化子)と考えるべきである。
"""

"""
1つのクラスから多数のオブジェクトを作られるが、Pythonがデータをオブジェクトとして実装していることを思い出そう。だから、クラス自体も
オブジェクトなのである。しかし、プログラム内のクラスオブジェクトは1つだけである。ここでしたようにclass catを定義した場合、映画『ハイランダー』
の不死のハイランダーと同じでCatのクラスオブジェクトは1つしか存在しえない。
"""
