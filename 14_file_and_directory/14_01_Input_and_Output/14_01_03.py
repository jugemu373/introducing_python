# write()によるテキストファイルへの書き込み
"""
print()を使って、ファイルに1行書き込みをしたが、write()でも書き込むことができる。
"""
poem = """There esd young lady named Bright,
Whose speed was far faster than light;
She started one day
In a relative way,
And returned on the previous night."""
print(len(poem))

"次のコードは、1つの呼び出しだけで詩全体をrelativityファイルに書き込む"
fout = open('relativity', 'w')
fout.write(poem)
fout.close()

"""
write()は、書き込んだバイト数を返す。print()のようにスペースや改行を追加したりしない。
先ほどと同じように、print()でも複数行の文字列をテキストファイルに書き込める。
"""
fout = open('relativity', 'w')
print(poem, file=fout)
fout.close()

"""
write()とprint()のどちらを使うべきか。デフォルトでは、print()は個々の引数の後にスペース、全体の末尾に改行を追加する。
上の例では、print()はrelativityファイルに改行を追加している。print()をwrite()のように動作させるためには以下の2つの引数を渡す。

    sep(セパレータ。デフォルトでスペース' 'になる。)
    end(末尾の文字列。デフォルトでは改行'\n'になる。)

これらの引数として空文字列を指定すれば、デフォルトの動作を変えられる。
"""
fout = open('relativity', 'w')
print(poem, file=fout, sep='', end='')
fout.close()

"ソース文字列が非常に大きい場合は、全部書き込むまでチャンクに分けて書き込んでいくこともできる。"
fout = open('relativity', 'w')
size = len(poem)
offset = 0
chunk = 100
while True:
    if offset > size:
        break
    fout.write(poem[offset: offset + chunk])
    offset += chunk
fout.close()

"""
このコードは、最初に100字、次に残りの50字を書き込んだ。スライスを使えば、例外を発生させずに「末尾を超えて進む」ことができる。
relativityファイルが非常にたいせつなものなら、xモードを使えば上書きによってファイルを壊すことを防げる。
"""
# fout = open('relativity', 'x')
"この機能は、例外ハンドラとともに使うことができる"
try:
    fout = open('relativity', 'x')
    fout.write('stomp stomp stomp')
except FileExistsError:
    print('relativity already exists! That was a close one.')
