# selfの自己弁護
"""
インスタンスメソッドの第1引数としてselfを組み込まなければならないことは、インデントの強要と並んでPythonの欠点として批判されることがある。
Pythonは、このself引数を使って、適切なオブジェクトの属性とメソッドを見つけてくる。
"""


class Car:
    def exclaim(self):
        print("I'm a Car!")


a_car = Car()
a_car.exclaim()


"""
このコードでは、裏で以下のような処理を行っている。

・a_carオブジェクトのクラス(Car)を探し出す。
・Carクラスのexclaim()メソッドにself引数としてa_carオブジェクトを渡す。
"""

# 以下のコードでも、同じ結果を得ることができる。
Car.exclaim(a_car)
