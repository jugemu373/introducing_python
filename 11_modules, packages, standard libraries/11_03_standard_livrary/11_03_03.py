# OrderedDict()によるキー順のソート
"""
from collections import OrderDictで返される。
OrderedDict()は、キーが追加された順序が覚えていて、イテレータから同じ順序でキーを返す。

Python3.7以降、辞書は追加順にキーを管理するようになった。辞書のキーの順序が予測不能だった初期バージョンでは、
OrderedDict()が役に立ったが、Python3.7よりも前のPythonを使っている場合だけである。
"""