"""
名前はどこで使われているかによって別々のものを参照できる。Pythonプログラムは、
様々な名前空間を持つ。名前は名前空間の中で決まった意味を持ち、他の名前空間の
同じ名前とは無関係になる

各関数は、それぞれ専用の名前空間を定義する。メインプログラムで変数xを定義し、
関数内でxという名前の別の変数を宣言すると、2つのxは別々のモノを参照する。
しかし、この壁は突破できる、必要なら、様々な方法で他の名前空間の名前にアクセスできる。

プログラムのメイン部分は、グローバル名前空間を定義する。そのため、この名前空間の変数は、
グローバル変数と呼ばれる。

グローバル変数の値は、関数内から参照できる
"""

animal = 'fruitbat'


def print_global():
    print('inside print_global:', animal)


print('at the top level:', animal)
print_global()


"""
関数内でグローバル変数の値を取得した上で、さらに書き換えようとするとエラーが起きる
"""
# def change_and_print_global():
#     print('inside change_and_print_global:', animal)
#     animal = 'wombat'
#     print('after the change', animal)

"""
同じanimalという名前を持つが、先ほどと異なり、グローバル変数ではなく、
関数内だけで有効な別の変数を書き換えようとしたと解釈されている。
そのため、代入していない変数を先に参照したとしてエラーが起きるのだ。
しかし、次のように参照しないで値をセットすると問題は起きない。
"""
animal = 'fruitbat'


def change_local():
    animal = 'wombat'
    print('inside change_local:', animal, id(animal))


change_local()
print(animal)
print(id(animal))


"""
関数内からローカル変数ではなく、グローバル変数の方にアクセスするには、
globalキーワードを使って明示しなければならない(The Zen of Pythonの
「暗黙より明示の方がよい」)
"""
animal = 'fruitbat'


def change_and_print_global():
    global animal
    animal = 'wombat'
    print('inside change_and_print_global:', animal)


print(animal)
change_and_print_global()
print(animal)


"""
関数内でglobalと書かなければ、Pythonはローカル名前空間を使い、animal変数はローカルになる
関数が終わったら、ローカル変数は消えてなくなる。
"""

"""
Pythonは名前空間の内容にアクセスするための関数を2つ用意している

・locals()は、ローカル名前空間の内容を示す辞書を返す
・globals()は、グローバル名前空間の内容を示す辞書を返す
"""

animal = 'fruitbat'


def change_local():
    animal = 'wombat'  # ローカル変数
    print('locals:', locals())


print(animal)
change_local()
print('globals:', globals())
print(animal)
