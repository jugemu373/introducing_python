# setdefault()とdefaultdict()による存在しないキーの処理
"""
辞書に対して、存在しないキーにアクセスしようとすると例外が発生するが、辞書のget()関数を使ってキーが存在しない場合は
デフォルトのバリューを返すようにすれば、例外は避けられる。setdefault()関数はget()と似ているが、キーがなければ更に辞書に
要素を追加するところが異なる。
"""
periodic_table = {'Hydrogen': 1, 'Helium': 2}
print(periodic_table)

"キーが辞書になければ、新しいバリューとともに辞書に追加される"
carbon = periodic_table.setdefault('Carbon', 12)
print(carbon)
print(periodic_table)

"既存のキーに別のデフォルトバリューを代入しようとしても、元のバリューが返され、辞書は一切変更されない。"
helium = periodic_table.setdefault('Helium', 944)
print(helium)
print(periodic_table)

"""
defaultdict()も例外を防ぐという点では似ているが、辞書作成時にあらゆる新しいキーの為にあらかじめデフォルトバリューを設定するとこが異なる。
引数は関数である。
"""
from collections import defaultdict
periodic_table = defaultdict(int)
periodic_table['Hydrogen'] = 1
print(periodic_table['Lead'])
print(periodic_table)

"""
defaultdict()の引数は、バリューを定義していないキーに与えられる値を返す関数である。
"""
def no_idea():
    return 'Huh?'


bestiary = defaultdict(no_idea)
bestiary['a'] = 'Abominable Snowman'
bestiary['b'] = 'Basilisk'
print(bestiary['a'])
print(bestiary['b'])
print(bestiary('c'))


"""
int(), list(), dict()を使えば、これらの型のデフォルト値として空の値を返せる、int()は0、list()は空リスト、dict()は空辞書を返す。
デフォルト値引数を省略すると、新しいキーに与えられるデフォルトバリューはNoneになる。

なお、lambdaを使えば、defaultdict()呼び出しの中でデフォルト作成関数を定義できる。
"""
bestiary = defaultdict(lambda: 'Huh?')
print(bestiary['e'])

"int()は、独自カウンタを作るための手段になるえる。"
food_counter = defaultdict(int)
for food in ['spam', 'spam', 'eggs', 'spam']:
    food_counter[food] += 1


for food, count in food_counter.items():
    print(food, count)


