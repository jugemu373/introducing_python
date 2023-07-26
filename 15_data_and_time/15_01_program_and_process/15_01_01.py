# subprocessによるプロセスの変更
"""
今まで見てきたプログラムは、すべて独立したプロセスだった。しかし、標準ライブラリのsubprocessモジュールを使えば、
Pythonからほかの既存のプログラムが生成した出力(標準出力とエラー出力の両方)を知りたいだけなら、getoutput()を使えばよい。
以下のコードは、Unixのdataプログラムの出力を取り出している。
"""
import subprocess
ret = subprocess.getoutput('date')
print(ret)

"""
プロセスが終了するまで情報は何も返されない。時間がかかりそうなプログラムを呼び出さなければならないときには、並行処理のことを
学んだ方がよい。getoutput()の引数は、完全なシェルコマンドを表す文字列なので、引数、パイプ、<と>のI/Oリダイレクトなどを入れることができる。
"""
ret = subprocess.getoutput('date -u')
print(ret)

"この出力文字列をwcコマンドにパイプを介して渡すと、1行6語29字と計算される"
# ret = subprocess.getoutput('date -u | wc')
# print(ret)

"check_output()は、コマンドと引数のリストを受け付ける。デフォルトではシェルを使わず、文字列ではなくbytes形式で標準出力だけを返す。"
# ret = subprocess.check_output(['date', '-u'])
# print(ret)

"ほかのプログラムの終了ステータスを見たいときには、getstatusoutput()を呼び出すと、ステータスコードと出力のタプルが返される。"
ret = subprocess.getstatusoutput('date')
print(ret)

"出力を受け取って処理する必要はなく、ただ終了ステータスだけを知りたいときは、call()を使えばよい。"
# ret = subprocess.call('date')
# print(ret)

"""
Unix系のシステムでは、通常は終了ステータス0が成功を表す。
返されてきた日時情報は出力に表示されるが、呼び出し元プログラムには渡されない。そこで、代わりに終了ステータスをretに保持している。
引数を取るプログラムは2通りの方法で実行できる。1つは、1個の文字列で全部を指定する方法だ。現在の日時をUTCで表示するdate -uコマンドを使って
試してみる。
"""
# 1
ret = subprocess.call('date -u', shell=True)

# 2
ret = subprocess.call(['data', '-u'])
