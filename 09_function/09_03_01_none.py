# NoneはPythonの特殊な値であり、何も言うべきことがないときに使われる
# Noneは、ブール値として評価すると偽になるが、ブール値のFalseと同じではない
thing = None
if thing:
    print("It's some thing")
else:
    print("It's no thing")


thing = None
if thing is None:
    print("It's nothing")
else:
    print("It's something")


# Noneは、空の値と欠損値を区別するために必要
# 値ゼロの整数と浮動小数点数、空文字列('')、空リスト([])、空タプル(())、空辞書({})、空集合(set())はどれもFalseだが、Noneとは等しくない
# 引数がNone, True, Falseのどれかを表示する関数
def whatis(thing):
    if thing is None:
        print(thing, "is None")
    elif thing:
        print(thing, "is True")
    else:
        print(thing, "is False")


print(whatis(None))
print(whatis(True))
print(whatis(False))
print(whatis(0))
print(whatis(0.0))
print(whatis(''))
print(whatis(""""""))
print(whatis(()))
print(whatis([]))
print(whatis({}))
print(whatis(set()))
print(whatis(0.00001))
print(whatis([0]))
print(whatis[''])
print(whatis('  '))
