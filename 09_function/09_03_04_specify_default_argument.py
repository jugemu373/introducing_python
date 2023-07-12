# デフォルト引数値の指定
# 仮引数にデフォルト値を指定することができる
# デフォルト値は、呼び出し元が対応する実引数を渡してこなかったときに使われる

# デフォルト引数の値が計算されるのは、関数が実行されたときではなく、定義されたタイミングである

def menu(wine, entree, dessert='pudding'):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}


# dessert引数を指定せずにmenu()を呼び出す
print(menu('chardonnay', 'chicken'))


# 引数を指定すれば、それがデフォルト値の代わりに使われる
print(menu('dunkelfelder', 'duck', 'doughnut'))


# 空のresultリストを毎回もらって実行されることを想定した関数
# バグ
# リストが空なのは、初めて呼びだされた時だけ
# 2回目に呼び出されたとき、resultには前回の呼び出しでセットされた1個の要素がまだ残っている
def buggy(arg, result=[]):
    result.append(arg)
    print(result)

print(buggy('a'))
print(buggy('b'))


# 意図した結果を出力するためには以下のように記述をする
def works(arg):
    result = []
    result.append(arg)
    return result


print(works('a'))
print(works('b'))


# 最初の呼び出しだということを示す別のものを渡すという方法もある
def nonbuggy(arg, result=None):
    if result is None:
        result = []
    result.append('a')
    print(result)


print(nonbuggy('a'))
print(nonbuggy('b'))
