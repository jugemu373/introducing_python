# remove()によるファイルの削除
"""
以下のコードは、remove()を使ってoops.txtを削除する。
"""
import os
os.remove('oops.txt')
print(os.path.exists('oops.txt'))
