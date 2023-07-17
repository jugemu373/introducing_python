# ダックタイピング
"""
Pythonは、ポリモーフィズムの穏やかな実装を持つ。クラスの種類に関わらず、メソッドの名前と引数に基づき、異なる
オブジェクトに対して同じ操作を適用するのである。

同じ__init__()メソッドを共有する3種類のQuoteクラスを定義する。
以下のクラスには、次の2つの関数を追加する。

・who()は、保存されているperson文字列の値を単純に返す。
・says()は、保存されているwordsにクラスごとに異なる記号を付けて返す。
"""


class Quote:
    def __init__(self, person, words):
        self.person = person
        self.words = words

    def who(self):
        return self.person

    def says(self):
        return self.words + '-'


class QuestionQuote(Quote):
    def says(self):
        return self.words + '-'


class ExclamationQuote(Quote):
    def says(self):
        return self.words + '!'


"""
QuestionQuoteやExclamationQuoteの初期化の方法はQuoteと変わらないので、__init__()メソッドのオーバーライドはしていない。
そこで、Pythonは、インスタンス変数のpersonとwordの保存のために自動的に親クラスのQuoteの__init__()メソッドオブジェクトの
self.wordsにアクセスできるのはそのためだ。
"""

hunter = Quote('Elmer Fudd', "I'm hunting wabbits")
print(hunter.who(), 'says:', hunter.says())
hunted1 = QuestionQuote('Bugs Bunny', "What's up, doc")
print(hunted1.who(), 'says:', hunted1.says())
hunted2 = ExclamationQuote('Daffy Duck', "It's rabbit season")
print(hunted2.who(), 'says:', hunted2.says())


"""
異なる3種類のsaysメソッドが3つのクラスのために異なる動作を提供する。これがオブジェクト指向言語の伝統的なポリモーフィズムである。
Pythonはそこからさらに少し進んで、who()、says()メソッドを持ちさえすればどのようなオブジェクトであっても(つまり、継承などを利用しなくても)、
これらのメソッドを実行できるようにしている。
"""


class BabblingBrook:
    def who(self):
        return 'Brook'
    def says(self):
        return 'Babble'
    

brook = BabblingBrook()

"""
そして、さまざまのオブジェクトのwho(), says()メソッドを実行してみる、
"""

def who_says(obj):
    print(obj.who(), 'says', obj.says())

who_says(hunter)
who_says(hunted1)
who_says(hunted2)
who_says(brook)


"""
このような動作は、古いことわざにちなんでダックタイピングと呼ばれる。

    アヒルのように歩き、
    アヒルのようにクワッと鳴くなら
    それはアヒルだ。
    - 賢者
"""