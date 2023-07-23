# bytesとbytearray
"""
Python3は、0から255までの値を取る。8ビット整数のシーケンスを2種類導入した。

・bytesはイミュータブルで、バイトのタプルのようなものだ。
・bytearrayはミュータブルで、バイトのリストのようなものだ。

以下のコード例では、リストblistからスタートして、the_bytesというbytes変数とthe_byte_arrayというbytearray変数を作る。
"""
blist = [1, 2, 3, 255]
the_bytes = bytes(blist)
print(the_bytes)
the_byte_array = bytearray(blist)
print(the_byte_array)

"""
bytes値を表現する時には、bを先頭として次にクォート文字、その後に\x02やASCII文字を並べ、最後に先頭に対応するクォート文字を置く。
Pythonは、16進シーケンスやASCII文字を1バイトずつ整数に変換するが、有効なASCIIエンコーディングにもなっているバイト値はASCII文字で表示する。
"""
print(b'\x61')
print(b'\x01abc\xff')

"以下のコード例は、bytes変数を書き換えられないことを示している。"
blist = [1, 2, 3, 255]
the_bytes = bytes(blist)
# the_bytes[1] = 127    # TypeErrorをスロー

"bytearray変数ならミュータブルであるから可能である。"
blist = [1, 2, 3, 255]
the_byte_array = bytearray(blist)
print(the_byte_array)
the_byte_array[1] = 127
print(the_byte_array)

"以下のコードは、どちらも0から255までの値の256個の要素を持つオブジェクトを作る。"
the_bytes = bytes(range(0, 256))
the_byte_array = bytearray(range(0, 256))

"""
bytes, bytearrayデータを表示するとき、Pythonは印字不能バイトについては\xxx形式を使い、印字可能バイトについては対応するASCIIを表示する
(一部のエスケープ文字も印字可能バイトと同様。例えば、\x0aではなく\nを表示する。)
"""
print(the_bytes)
"しかし、これらはバイト(小さな整数)であり文字ではないので、この表示はすこし紛らわしい。"
