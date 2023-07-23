# パターン: マッチした文字列の出力の指定
"""
match()やsearch()を使ったときは、結果オブジェクトのmからm.group()という形ですべてのマッチを取り出すことができる。
パターンを()で囲むと、マッチは独自のグループに保存される。
以下に示すように、m.groups()を呼び出せば、それらのタプルを得られる。
"""
import re

source = """I wish I may, I wish I might
Have a dish of fish tonight"""
m = re.search(r'(.dish\b).*(\bfish)', source)
print(m.group())
print(m.groups())
"""
(?P<name>expr)という形式を使うと、exprにマッチした部分はnameという名前のグループに保存される。
"""
m = re.search(r'(?P<DISH>.dish\b).*(?P<FISH>\bfish)', source)
print(m.group())
print(m.groups())
print(m.group('DISH'))
print(m.group('FISH'))
