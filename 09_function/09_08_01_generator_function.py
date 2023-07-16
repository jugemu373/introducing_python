# ジェネレータ関数は、大きくなる可能性があるシーケンスを作りたいときに使える
# 値をreturnで返す代わりにyield文で返すことを除けば、通常の関数と同じ
def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step


# my_rangeは通常の関数である
print(my_range)
# ジェネレータオブジェクトを返す
ranger = my_range(1, 5)
print(ranger)

# ジェネレータオブジェクトを対象として反復処理できる
for x in ranger:
    print(x)


"""
ジェネレータは一度しか実行できない。リスト、集合、文字列、辞書は
メモリ内にあるが、ジェネレータはその場で値を作り、イテレータを介
して一度に1つずつ値を返してくる。ジェネレータは生成した値を覚え
ていないので、ジェネレータを再起動したり、バックアップする
ことはできない。
"""

for try_again in ranger:
    print(try_again)
