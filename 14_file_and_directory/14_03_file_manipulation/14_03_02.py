# isfile()によるファイルのタイプチェック
"""
この節の関数は、名前がファイル、ディレクトリ、シンボリックリンクのどれを参照しているのかをチェックする。

isfile()は、引数が昔ながら普通のファイルかという問いに答える。
"""
import os
name = 'oops.txt'
print(os.path.isfile(name))

"ディレクトリかどうかは以下のようにすればわかる。"
print(os.path.isdir(name))

"""
.1個はカレントディレクトリを表し、..は親ディレクトリを表す。
これらは必ず存在するので、以下のような文は必ずTrueを返してくる。
"""
print(os.path.isdir('.'))

"""
osモジュールには、パス名を扱う関数が多数含まれている。そのような関数の1つであるisabs()は、引数が絶対パス名
(フルパス名。先頭が/ですべての親が含まれているもの)かどうかを返してくる。
引数は実際に存在するファイル名なくても構わない。
"""
print(os.path.isabs(name))
print(os.path.isabs('/big/fake/name'))
print(os.path.isabs('big/fake/name/without/a/leading/slash'))
