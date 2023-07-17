# 特殊メソッド
"""
a = 3 + 8 のようなコードを入力したとき、値3や8を持つ整数オブジェクトは、+の実装法をどのようにして知るのだろうか。
また、name = "Daffy" + "" + "Duck"と入力したとき、+が今度は文字列の連結の意味で使われていることをPythonはどのようにして
知るのだろうか。そして、aとnameは、計算結果を得るための=の使い方をどのようにして知るのだろうか。
これらの演算子には、特殊メソッドを使うとたどり着く(同じものがマジックメソッドと呼ばれている場合もある。)

これらのメソッドの名前は、先頭と末尾が__になっているが、それはプログラマが自分の変数名でこのような使うことはないだろうという理由からだ。
こういうメソッドは今までにも登場している。__init__()は、クラス定義と渡された引数をもとに新しく作成されたオブジェクトを初期化する。
また、「10.5.5 属性を隠すための名前のマングリング」では、ダンダー名によってメソッド、属性の名前がマングリングされることを説明した。
"""


class Word:
    def __init__(self, text):
        self.text = text

    def equals(self, word2):
        return self.text.lower() == word2.text.lower()


"そして、3つの異なる文字列から3このWordオブジェクトを作る。"
first = Word('ha')
second = Word('HA')
third = Word('eh')

"文字列'ha'と文字列'HA'は、小文字に変換してから比較すれば、等しくなる。"
first.equals(second)
"しかし、文字列'eh'と文字列'ha'は同じにならない。"
first.equals(third)


"""
この小文字への変換と比較を実行するようになるequals()メソッドを定義したが、Pythonの組み込み型と同じように、
if first == secondと書ければ便利である。ではその仕事に取り掛かる。
"""


class Word:
    def __init__(self, text):
        self.text = text

    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()


first = Word('ha')
second = Word('HA')
third = Word('eh')
print(first == second)
print(first == third)


"""
__eq__()は、Pythonの等価比較の特殊メソッドである。
ほかの特殊メソッドを以下にまとめる

比較のための特殊メソッド
__eq__(self, other)     self == other
__ne__(self, other)     self != other
__li__(self, other)     self < other
__gt__(self, other)     self > other
__le__(self, other)     self <= other
__ge__(self, other)     self >= other


算術計算のための特殊メソッド
__add__(self, other)    self + other
__sub__(self, other)    self - other
__mul__(self, other)    self * other
__floordiv__(self, other)   self // other
__truediv__(self, other)    self / other
__mod__(self, other)    self % other
__pow__(self, other)    self ** other

算術計算ための特殊メソッドの用途は、数値だけに限らわない。たとえば、Pythonの文字列オブジェクトは+を連結のために、
*を繰り返しの為に使っている。特殊メソッド名は他にもたくさんあり、特殊メソッド名でドキュメントされている。


その他の特殊メソッド
__str__(self)   str(self)
__repr__(self)  repr(self)
__len__(self)   len(self)

__init__()を別にすれば、もっともよく使われているのは__str__()かもしれない。オブジェクトを表示するときには、これを使う。
このメソッドは、print(), str(), その他5章で説明した文字列フォーマット関数で使われている。対話型インタープリタは、
__repr__()関数を使って変数をエコー出力している。__str__()または__repr__()を定義し忘れていると、Pythonが定義している
オブジェクトのデフォルトの文字列バージョンが使われている。
"""
first = Word('ha')
print(first)


"""それでは、Wordクラスに__str__(), __repr__()メソッドを追加する"""


class Word:
    def __init__(self, text):
        self.text = text

    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()

    def __str__(self):
        return self.text

    def __repr__(self):
        return 'Word("' + self.text + '")'


first = Word('ha')
first   # __repr__()を使う
print(first)    # __str__()を使う
