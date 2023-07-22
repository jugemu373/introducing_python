# search()による最初のマッチの検索
"""
search()を使えば、.*というワールドカードを使わずに、ソース文字列'Young Frankenstein'の意味の位置にあるパターン'Frank'を探せる。
"""
import re
source = 'Young Frankenstein'
m = re.search(r'Frank', source)
if m:   # searchはオブジェクトを返す
    print(m.group())
