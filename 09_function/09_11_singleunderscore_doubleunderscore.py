"""
先頭と末尾が2個の__になっている名前は、Pythonが使う変数として予約されている。
自分自身の変数としてこの種のものを使ってはならない。このパターンが選ばれたのは、
アプリケーション開発者が自分の変数のためにこのような名前を選ぶことはないだろうと考えたから

関数の名前は、システム変数のfunction.__name__
docstringは、function.__doc__
"""
def amazing():
    """これは素晴らしい関数だ。
    もう一度見る?"""
    print('この関数の名前:', amazing.__name__)
    print('関数のdocstring:', amazing.__doc__)


amazing()


