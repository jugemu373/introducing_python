"""
今までは何かを直接行うために関数を呼び出しており、関数からよびだされていたのは
おそらく他の関数だった。しかし、関数が自分自身を呼び出すとどうなるだろうか。
このような関数呼び出しを再起と呼ぶ。whileやforの無限ループを避けたいのと同じように、
無限再起は避けたいところだ。

Pythonは再起が深くなりすぎると例外を送出してくれる
"""
# def dive():
#     return dive()


# dive()
# RecursionError: 再起の最大深度を超えた


"""
再起は、リストのリストのリストのような「平坦ではない」データを処理するときに役立つ。
リストのすべてのサブリストをネストの深さに関わらず「平坦化」したいものとする
"""


def flatten(lol):
    """Pythonプログラマの面接の頻出問題"""
    for item in lol:
        if isinstance(item, list):
            for subitem in flatten(item):
                yield subitem
        else:
            yield item


lol = [1, 2, [3, 4, 5], [6, [7, 8, 9], []]]
print(list(flatten(lol)))


def flatten(lol):
    """Python3.3でジェネレータが他のジェネレータに仕事の一部を委ねるyield from式が追加された。
    これを使えば、flatten()を単純化できる"""
    for item in lol:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item


lol = [1, 2, [3, 4, 5], [6, [7, 8, 9], []]]
print(list(flatten(lol)))
