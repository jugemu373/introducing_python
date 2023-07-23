# その他のバイナリデータツール
"""
サードパーティのオープンソースパッケージには、以下のようなものがある。
この中には、バイナリデータの定義や抽出方法をより宣言的に行うパッケージもある。

・bitstring
・consturct
・hachoir
・binio
・kaitai struct

以下のコードでは、constructが必要になる。
constructを使った場合、dataからPNGのサイズ情報を抽出するには次のようにする。
"""
from construct import Const, Magic, String, Struct, UBInt32
fmt = Struct('png',
             Magic(b'\x89PNG\r\n^x1a\n'),
             UBInt32('length'),
             Const(String('type', 4), b'IHDR'),
             UBInt32('width'),
             UBInt32('height')
             )
data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR' + \
    b'\x00\x00\x00\x9a\x00\x00\x00\x8d\x08\x02\x00\x00\x00\xc0'
result = fmt.parse(data)
print(result)
print(result.width, result.height)
