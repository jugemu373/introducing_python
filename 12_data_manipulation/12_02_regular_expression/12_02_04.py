# split()によるマッチを利用した分割
"""
単純な文字列ではなく、パターンで文字列を分割し、部分文字列のリストを作る方法を示す。
"""
import re
source = 'Young Frankenstein'
m = re.split(r'n', source)
print(m)    # splitはリストを返す
