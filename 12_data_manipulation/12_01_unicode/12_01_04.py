# デコーディング
# デコーディングは、バイト列をUnicode文字列にする操作である。なんらかの外部ソース(ファイル、データベース、ウェブサイト、ネットワークAPIなど)
# からテキストを取り出したとき、そのテキストはバイト列としてエンコードされている。難しいのは、実際にどのエンコーディングを使われているのを知ることだ。
# それがわからなければ、エンコーディングの逆をやって、Unicode文字列を得ることができない。
# しかし、バイト列自体の中には、どのエンコーディングが使われているかを教えてくれるものはない。
place = 'caf\u00e9'
print(place)
print(type(place))
# UTF-8でエンコードしてplace_bytesというbytes変数に格納
place_bytes = place.encode('utf-8')
print(place_bytes)
print(type(place_bytes))
# バイト列をUnicode文字列にデコード
place2 = place_bytes.decode('utf-8')
print(place2)
# utf-8でエンコードしたバイト列を他のエンコードからの形式でデコードするとUnicodeDecodeErrorが発生する。
# place3 = place_bytes.decode('ascii')
# ASCIIデコーダは、0xc3というバイト値がASCIIでは無効なので例外を送出している。
# 8ビットキャラクタセットのエンコーディングでは、128(16進80)から255(16進FF)までの有効な値を持つものがあるが、それはUTF-8と異なる値だ。
place4 = place_bytes.decode('latin-1')
print(place4)
place5 = place_bytes.decode('windows-1252')
print(place5)
