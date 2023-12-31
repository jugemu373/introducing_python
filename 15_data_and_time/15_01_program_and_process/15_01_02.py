# multiprocessingによるプロセスの作成
"""
multiprocessingモジュールを使えば、Python関数を別個のプロセスとして実行できる。1つのプログラムから複数の独立した
プロセスを実行することさえできる。以下は、短くて単純なプログラムである。
ファイルmp.pyに保存し、python mp.py と入力して実行する。
"""

"""
Process()クラスは、新しいプロセスを起動し、その中でwhoami()を実行する。この処理は4回繰り返されるループで実行されているので、
whoami()を実行し、終了する新しいプロセスを4個作っている。

multiprocessingモジュールには、目を引く機能がもっとたくさんある。本来このモジュールは、処理時間全体を短縮するために、
複数のプロセスに処理を下請けに出さなければならないときのために作られたものだ。たとえば、スクレイプするウェブページのダウンロードや
イメージのサイズ変更などである。タスクをキューイングして、プロセス間通信を有効にすることや、すべてのプロセスの終了を待つこともできる。
"""
