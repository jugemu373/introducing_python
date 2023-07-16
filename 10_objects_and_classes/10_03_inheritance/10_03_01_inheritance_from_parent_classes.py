"""
新クラスでは、追加、変更したい部分だけを定義する。すると、この定義が実際に使われ、オーバーライド(置き換えられた)
古いクラスの動作は使われない。元のクラスは親、スーパークラス、基底クラス、新しいクラスは子、サブクラス、派生クラスと呼ばれる。
"""
# 親クラスとなるCarを作成
class Car():
    pass


# Carクラスを継承するYugoというサブクラスを作成
class Yugo(Car):
    pass


"クラスが他のクラスを継承したものかどうかは、issubclass()を使えば調べられる。"
issubclass(Yugo, Car)

"次にそれぞれのクラスからオブジェクトを作る。"
give_me_a_car = Car()
give_me_a_yugo = Yugo()

"""
子クラスは、親クラスを専門特化したものである。これをオブジェクト指向の専門用語では、「YugoはCarである」を満たすis-a関係だという。
give_me_a_yugoオブジェクトはYugoクラスのインスタンスだが、Carができることを継承してもいる。
"""

class Car():
    def exclaim(self):
        print("I'm a Car!")


class Yugo(Car):
    pass


give_me_a_car = Car()
give_me_a_yugo = Yugo()
give_me_a_car.exclaim()
give_me_a_yugo.exclaim()


"""
継承は魅力的だが、やりすぎになることがある。長年にわたるオブジェクト指向プログラミングの実戦経験から、継承を使いすぎるとプログラムが
管理しにくくなる場合があるということがわかっている。継承ばかりに頼るよりも、集約やコンポジションといったほかのテクニックも検討すべき
であると言われている。
"""
