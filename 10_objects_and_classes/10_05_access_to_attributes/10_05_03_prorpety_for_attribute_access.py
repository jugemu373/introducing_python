# 属性アクセスのためのプロパティ
"""
属性の非公開化のためのパイソニックな方法は、プロパティである。

プロパティには2種類の実装方法がある。
第1の方法は、先ほどのDuckクラスの定義の最後の行として、name = property(get_name, set_name)という文を追加する
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

    name = property(get_name, set_name)


don = Duck('Donald')
don.get_name()
don.set_name('Donna')
don.get_name()


"hidden_nameの取得、設定の為にnameプロパティも使えるようになった"
don = Duck('Donald')
don.name
don.name = 'Donna'
don.name


"""
第2の方法では、メソッドget_name、set_nameをただのnameに変更して次のようなデコレータを追加する。

・@property: ゲッターメソッドの前に付けるデコレータ
・@name.setter: セッターメソッドの前に付けるデコレータ
"""


class Duck:
    def __init__(self, input_name):
        self.hidden_name = input_name

    @property
    def name(self):
        print('inside the getter')
        return self.hidden_name

    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name


fowl = Duck('Howard')
fowl.name
fowl.name = 'Donald'
fowl.name
