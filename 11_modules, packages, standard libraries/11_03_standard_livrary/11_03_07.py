# ランダムな値
"""
random.choice()を使った。この関数は、引数のシーケンス(リスト、タプル、辞書、文字列)から値を1つランダムに選んで返す。
"""
from random import choice, sample, randint, randrange, random


print(choice([23, 9, 46, 'bacon', 0x123abc]))
print(choice('a', 'one', 'and-a', 'two'))
print(choice(range(100)))
print(choice('alphabet'))

"sample()を使えば、複数の値をまとめて返せる。"
print(sample([23, 9, 46, 'bacon', 0x123abc], 3))
print(sample('a', 'one', 'and-a', 'two', 2))
print(sample(range(100), 4))
print(sample('alphabet', 7))

"任意の範囲からランダムな整数を取り出したいときには、randint()やrandrange()を使う。"
print(randint(38, 74))
print(randrange(38, 74))

"randrange()は、range()と同様に、先頭と末尾を指定する整数引数を取り、オプションでステップを指定する整数引数を取る。"
print(randrange(38, 74, 10))
print(randrange(38, 74, 10))

"0.0から1.0までのランダムな浮動小数点数を得る関数もある。"
print(random())
