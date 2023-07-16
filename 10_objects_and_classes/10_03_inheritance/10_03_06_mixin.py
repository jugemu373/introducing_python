# ミックスイン
"""
クラス定義にヘルパとして使うだけの親クラスを組み込むことができる。
つまり、ほかの親クラスとはメソッドを共有せず、メソッドの解決の曖昧さを解決できる。

このような親クラスはミックスインクラスと呼ばれることがあり、ロギングなどの「副次的な」タスクを追加するために使われる事が多い。
"""

import pprint


class PrettyMixin:
    def dump(self):
        pprint.pprint(vars(self))


class Thing(PrettyMixin):
    pass


t = Thing()
t.name = "Nyarlathotep"
t.feature = "ichor"
t.age = "eldritch"
t.dump()
