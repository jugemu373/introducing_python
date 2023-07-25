# copy()によるコピー
"""
copy()はshutilという別のモジュールに含まれている。
以下のコード例は、oops.txtファイルをコピーする。
"""
import shutil

shutil.copy('oops.txt', 'ohno.txt')
"shutil.move()は、ファイルをコピーしてからオリジナルを削除する。"
