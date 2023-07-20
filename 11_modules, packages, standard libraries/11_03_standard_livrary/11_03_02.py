# Counter()による要素数の計算
"""
Python標準ライブラリには、さらに多くの機能を持った関数が含まれている。
"""
from collections import Counter

breakfast = ['spam' 'spam', 'egg', 'spam']
breakfast_counter = Counter(breakfast)
print(breakfast_counter)

"most_common()は、すべての要素を降順で返す。引数として整数を指定すると、最上位から数えてその個数分だけを表示する。"
print(breakfast_counter.most_common())
print(breakfast_counter.most_common(1))

"カウントを結合することもできる。まず、breakfast_counterの内容を確認しておく。"
print(breakfast_counter)
print(Counter({'spam': 3, 'eggs': 1}))

lunch = ['eggs', 'eggs', 'bacon']
lunch_counter = Counter(lunch)
print(lunch_counter)

"2つのカウンタを結合する第1の方法は、+を使った加算。"
print(breakfast_counter + lunch_counter)

"片方からもう片方を引くには、-を使う。"
print(breakfast_counter - lunch_counter)
print(lunch_counter - breakfast_counter)

"積集合演算子の&を使えば、共通要素が得られる。"
print(breakfast_counter & lunch_counter)

"和集合演算子 | を使えば、すべての要素を得ることができる。"
print(breakfast_counter | lunch_counter)
