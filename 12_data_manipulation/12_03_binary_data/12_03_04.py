# binasciiによるバイト/文字列の変換
# """
# 標準ライブラリのbinasciiモジュールには、バイナリデータとさまざまな文字列表現を相互変換する関数が含まれている。16進(base16)、
# base64、uuencodedなどだ。例えば、以下のコードは、Pythonがbytes変数を表示するときに使っている\xxxとASCIIの混合形式ではなく、
# 16進値のシーケンスという形で8バイトPNGヘッダを表示する。
# """
import binascii
valid_png_header = b'\x89PNG\r\n\x1a\n'
print(binascii.hexlify(valid_png_header))
print(binascii.unhexlify(valid_png_header))
