# super()による親への支援要請
"""
サブクラスのために__init__()メソッドを定義することは、親クラスの__init__()メソッドを置き換えようとしていることである。
親クラスバージョンはもう自動的に呼び出されなくなる。親クラスのバージョンを呼び出したければ、明示的に呼び出さなければならない。
"""


class Person:
    def __init__(self, name):
        self.name = name


class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email


"""
・super()が親クラスのPersonの定義を取り出す。
・super().__init__()メソッド呼び出しは、Person.__init__()メソッドを呼び出す。この時、self引数の親クラスへの受け渡しはPythonが処理するので、
プログラマはオプションの引数を適切に渡すことだけをきちんとやればよい。
"""


bob = EmailPerson('Bob Frapples', 'bob@frapples.com')
print(bob.name)
print(bob.email)
