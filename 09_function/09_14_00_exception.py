"""
例外とは、エラーが起きたときに実行されるコードのこと。

リストやタプルに範囲外の位置を指定してアクセスしようとしたときや、
存在しないキーで辞書にアクセスしようとしたときなどに例外が発生する。

特定の条件の元では失敗するコードを実行するときには、適切な例外ハンドラを作って、
起こる可能性のあるエラーをすべてキャッチする必要がある。

例外が発生しそうなところにはすべて例外処理を追加して、ユーザに何が起きるのかを
知らせるようにするのがグッドプラクティスであるとされている。
問題を解決できなくても、少なくとも状況を知らせて穏便にプログラムを終了させることはできる。

ある関数で例外が発生し、その関数で例外をキャッチしなければ、上位の関数の対応するハンドラが
キャッチするまで例外は浮上していく。プログラム内で独自の例外ハンドラを用意できていなければ、
次のコードが示すように、Pythonはエラーメッセージとエラー発生個所について
情報を出力し、プログラムを強制終了する。
"""
short_list = [1, 2, 3]
position = 5
short_list[position]
