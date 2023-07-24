# read(), readline(), readlines()によるテキストファイルの読み出し
"""
引数無しでread()を呼び出せば、ファイル全体を一度い読みだすことができる。
(サイズの大きいファイルでこれを使う場合は注意が必要。1GBのファイルは1GBのメモリを消費する。)
"""
fin = open('relativity', 'r')
poem = fin.read()
fin.close()
print(len(poem))

"""
次数の上限を指定すれば、read()が一度に返すデータの量を制限できる。100文字ずつ読み、
その後のチャンクを文字列のpoemに追加して元のデータを再現する。
"""
poem = ''
fin = open('relativity', 'r')
chunk = 100
while True:
    fragment = fin.read(chunk)
    if not fragment:
        break
    poem += fragment
fin.close()
print(len(poem))

"""
ファイルをすべて読み込んだ後で更にread()を呼び出すと、空文字列('')が返される。これはif not fragmentではFalseとして扱われ、
while Trueループは終わる。

readline()を使えば、フィイルを1行ずつ読みだすことができる。
以下の例では、poemに各行を追加して、オリジナルを再現する。
"""
poem = ''
fin = open('relativity', 'r')
while True:
    line = fin.readline()
    if not line:
        break
    poem += line
fin.close()
print(len(poem))

"""
ファイルをすべて読むと、readline()もread()と同様に空文字列を返し、これがFalseとして評価される。
テキストファイルをもっとも簡単に読みだせるのは、イテレータを使った方法である。
イテレータは一度に1行ずつ返す。前のコードとよく似ているがコード量は少ない。
"""
poem = ''
fin = open('relativity', 'r')
chunk = 100
for line in fin:
    poem += line
fin.close()
print(len(poem))

"""
今までのコード例は、どれも最終的にはpoemという1個の文字列変数を組み立てる。
それに対し、readlines()は一度に1行ずつ読み出して、1行文字列のリストを返す。
"""
fin = open('relativity', 'r')
lines = fin.readlines()
fin.close()
print(len(lines), 'lines read')
for line in lines:
    print(line, end='')


"""
最初の4行はすでに改行が含まれているので、print()には自動改行をしないように指示している。
しかし、最後の行には改行が含まれていないので、最後の行を出力すると、そのすぐ後に対話型インタプリンタのプロンプトが表示されている。
"""
