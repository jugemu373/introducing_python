# ジェネレータは、Pythonのシーケンスを作成するオブジェクトである
# ジェネレータを使えば、シーケンス全体を一度に作ってメモリに格納しなくてもシーケンスを反復処理できる
# ジェネレータはイテレータのデータソースになることが多い
# ジェネレータは、反復処理のたびに、最後に呼び出されたときにどこにいたかを管理し、次の値を返す
# range()はｍジェネレータの1つである
# Python2では、range()はリストを返すが、それではメモリに収まる以上の整数を生成できない
# Python2には、ジェネレータのxrange()もあるが、Python3では、それが普通のrange()に変更された
sum(range(1, 101))