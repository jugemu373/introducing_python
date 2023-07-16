# ゲッターとセッター
"""
オブジェクト指向言語の中には、外部から直接アクセスできない非公開のオブジェクト属性をサポートしているものがある。
プログラマは、そのような非公開属性の値を読み書きするゲッター、セッターメソッドを書かなければならない時がある。

Pythonは非公開属性を持っていないが、属性名を少し非公開っぽくわかりにくくした上でゲッター、セッターを書くことはできる
(ただし、最良の方法は、プロパティである)。
"""


class Duck:
    def __init__(self, input_name):
        self.hidden_name = input_name

    def get_name(self):
        print('inside the getter')
        return self.hidden_name

    def set_name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name


don = Duck('Donald')
print(don.get_name())
don.set_name('Donna')
print(don.get_name())
