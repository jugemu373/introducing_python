# モジュール検索パス
"""
Pythonは、カレントディレクトリからスタートしてサブディレクトリchoicesとその中のモジュールを探すと説明したが、
実際にはほかの場所も参照するし、参照方法も制御できる。

先ほど、標準ライブラリのrandomモジュールからchoice()関数をインポートした。標準ライブラリはカレントディレクトリの
下にはないので、Pythonはほかの場所を探さなければならなかったはずだ。

Pythonインタプリタが参照するすべての場所は、標準ライブラリのsysモジュールをインポートしてそのpathを見ればわかる。
このpathは、Pythonがインポートするモジュールを探すために検索をかけるディレクトリ名とZIPファイル名のリストでは、
sys.pathは次のように定義されている。
"""
import sys
for place in sys.path:
    print(place)


"""
最初の空行は空文字列の '' で、カレントディレクトリという意味である。sys.pathの先頭が''なら、何かをインポートしようとしたときに、
Pythonはまずカレントディレクトリを見るようになる。import fastは、fast.pyを探す。これがPythonファイルを入れておけば、
import choices かfrom choices import fastでインポートできる。

使われるのは、最初にマッチしたファイルだ。そのため、自分でrandomというモジュールを定義し、それが標準ライブラリよりも
前の検索パスに含まれている場合、標準ライブラリのrandomにはアクセスできない。

検索パスはコード内で変更できる。例えば、Pythonにまず真っ先に/my/modulesディレクトリを参照してもらいたい場合には、次のようにする。
"""

sys.path.insert(0, "/my/modules")

