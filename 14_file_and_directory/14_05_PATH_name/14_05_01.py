# abspath()によるパス名の取得
"""
abspath()は、相対パスを絶対パスに展開する。カレントディレクトリが/usr/gaberluzieで、oops.txtがそこにある場合、
以下のようにすると、このファイルの絶対パスが返される。
"""
import os
print(os.path.abspath('oops.txt'))
