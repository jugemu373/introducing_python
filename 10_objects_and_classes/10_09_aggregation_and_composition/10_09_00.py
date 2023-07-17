# 集約とコンポジション
"""
継承は、子クラスにほとんどの場合に親クラスと同じ動作をさせたい(子が親であるというis-a関係がある)ときにはよいテクニックだ。
とかく、非常に凝った継承階層を作りたくなりがちだが、継承よりもコンポジション(合成)や集約のほうが理にかなっている場合がある。

どういう違いがあるのだろうか。コンポジションは、あるものが別のものの一部になっている関係がある。アヒルは鶏である(継承)と同時に、
しっぽを持つ(コンポジション。has-a関係)。しっぽはアヒルの一種ではなく、一部だ。
"""


class Bill:
    def __init__(self, description):
        self.description = description


class Tail:
    def __init__(self, length):
        self.length = length


class Duck:
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail

    def about(self):
        print('This duck has a', self.bill.description,
              'bill and a', self.tail.length, 'tail')


a_tail = Tail('Long')
a_bill = Bill('wide orange')
duck = Duck(a_bill, a_tail)
duck.about()


"""
集約は関係を表現するが、もっとも穏やかなものだ。あるものが別のものを使っている(use)が、両者は独立に存在する。
アヒルは湖を使うが、どちらかがどちらかの一部になっているわけではない。
"""
