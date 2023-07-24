# seek()による位置の変更
import os
"""
Pythonは、ファイルの読み書き中にファイル内のどこにいるのかを管理している。tell()は、ファイルの先頭からの現在のオフセットを
バイト単位で返す。seek()は、ファイル内の別のオフセットに移動する。つまり、ファイルの最後のバイトを読みだすためにファイルをすべて読み出す必要はない。
最後のバイトにseek()して、1バイトを読み出せばよいのである。
"""
fin = open('bfile', 'rb')
print(fin.tell())

"seek()を使って、ファイルの末尾の1バイト手前に移動する。"
print(fin.seek(255))

"""
seek()は、移動後のオフセットも返してくる。
seek()には、seek(offset, origin)のように第2引数を指定する事もできる。

    originが0(デフォルト)なら、先頭からoffsetバイトの位置に移動する。
    originが1なら、現在の位置からoffsetバイトの位置に移動する。
    originが2なら、末尾からoffsetバイトの位置に移動する。

これらの値は、標準ライブラリのosモジュールでも定義されている。
"""
print(os.SEEK_SET)
print(os.SEEK_CUR)
print(os.SEEK_END)

"最後のバイトは次のような方法でも読み出せる。まず、ファイルをバイナリモード、読み出し専用で開く。"
fin = open('bfile', 'rb')
print(fin.seek(-1, 2))
print(fin.tell())
bdate = fin.read()
print(len(bdate))
print(bdate[0])
"""
seek()を正しく動かすためにtell()を呼び出す必要はない。ここで単に両者が同じオフセットを返してくることを示したのみである。

ファイルの現在の位置からのシークの例も見てみる。
"""
fin = open('bfile', 'rb')

"ファイルの末尾の2バイト前に移動する。"
print(fin.seek(254, 0))
print(fin.tell())

"1バイト前進させてみる。"
print(fin.seek(1, 1))
print(fin.tell())

"ファイルの末尾まで読み出す。"
bdate = fin.read()
print(len(bdate))
print(bdate[0])

"""
これらの関数がもっとも役に立つのはバイナリファイルだ。テキストファイルでも使えるが、内容が1文字あたり1バイトの
ASCIIだけで書かれていない限り、オフセットの計算で苦労する。オフセット計算はテキストエンコーディングによって異なり、
もっともよく使われるエンコーディング(UTF-8)は、1文字あたりのバイト数が可変になっている。
"""
