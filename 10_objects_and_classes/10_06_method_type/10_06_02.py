# クラスメソッド
"""
インスタンスメソッドに対し、クラスメソッドはクラス全体に影響を与える。クラスに加えた変更は、すべてのオブジェクトに影響を与える。
クラス定義の中で、デコレータ@classmethodを入れると、その次のメソッドはクラスメソッドになり、メソッドの第1引数は、クラス自体になる。
Pythonの伝統では、この引数をclsと呼ぶことになっているが、それはclassが予約語でこのような場面では使えないからだ。
"""


class A:
    count = 0

    def __init__(self):
        A.count += 1

    def exclaim(self):
        print("I'm an A!")

    @classmethod
    def kids(cls):
        print("A has", cls.count, "little objects.")


easy_a = A()
breezy_a = A()
wheezy_a = A()
print(A.kids())


"""
self.count(これでは、インスタンス属性になってしまう)ではなく、A.count(クラス属性)を参照していることに注意。
kids()メソッドの中ではcls.countを使ったが、A.countを使ってもよかったところだ。
"""
