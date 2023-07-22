# sub()によるマッチした部分の置換
"これは文字列のreplace()と似ているが、置換対象としてリテラル文字列ではなくパターンを指定する。"
import re
source = 'Young Frankenstein'
m = re.sub(r'n', '?', source)
print(m)    # subは文字列を返す
