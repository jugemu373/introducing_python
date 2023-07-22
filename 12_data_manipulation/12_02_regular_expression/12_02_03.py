# findall()によるすべてのマッチの検索
"""
これまでのコード例は、1つのマッチが見つかったらそこで処理を終えていた。しかし、文字列の中に'n'という1文字の文字列が何個あるか
知りたい場合には以下のようにする。
"""
import re
source = 'Young Frankenstein'
m = re.findall(r'n', source)
print(m)    # findallはリストを返す
print('Found', len(m), 'matches')

"'n'の後ろに任意の文字が続いているものならどうか"
m = re.findall(r'n.', source)
print(m)

"""
最後の'n'にはマッチしていない。
これもマッチさせたければ、'n'の後の文字はオプションだということを示す?を使う必要がある。
"""
m = re.findall(r'n/.?', source)
print(m)
