# write()によるバイナリファイルの書き込み
"""
open()呼び出しのモード文字列に'b'を入れると、ファイルはバイナリモードが開かれる。この場合、文字列ではなくbytesを読み書きすることになる。
バイナリの詩はないので、0から255までの256バイトを生成する。
"""
bdata = bytes(range(256))
print(len(bdata))

"バイナリモードで書き込み用にファイルを開き、すべてのデータをまとめて書き込んでみる。"
fout = open('bfile', 'wb')
fout.write(bdata)
fout.close()

"""
この場合も、write()は書き込んだバイト数を返す。
テキストの場合と同様に、バイナリデータもチャンク単位で書き込むことできる。
"""
fout = open('bfile', 'wb')
size = len(bdata)
offset = 0
chunk = 100
while True:
    if offset > size:
        break
    fout.write(bdata[offset: offset + chunk])
    offset += chunk
fout.close()
