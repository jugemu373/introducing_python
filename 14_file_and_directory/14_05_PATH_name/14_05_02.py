# realpath()によるシンボリックリンクパス名の取得
"""
jeepers.txtという新ファイルを作った。このような場合、次のようにrealpath()を呼び出せば、jeepers.txtが参照しているoops.txtの名前が得られる。
"""
import os
print(os.path.realpath('jeepers.txt'))
