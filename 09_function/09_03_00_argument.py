# anythingという1個の引数を取る関数を定義する
def echo(anything):
    return anything + ' ' + anything


echo('Rumplestiltskin')

# 実引数(argument): 関数を呼び出す際に渡す値のこと
# 仮引数(parameter): 実引数を渡して関数を呼び出すとき、それらの値は関数内の対応する仮引数にコピーされる


def commentary(color):
    if color == 'red':
        return "It's a tomato"
    elif color == "green":
        return "It's a green pepper"
    elif color == "bee purple":
        return "I don't know what it is, but only bees can see it."
    else:
        return "I've never heard of the color " + color + "."


comment = commentary('blue')

# 関数内部のcolor仮引数に値'blue'を代入する
# if-elif-elseのコードを実行する
# 文字列を返す

print(comment)


# 関数は、任意の型の引数を0を含む、いくつでも受け付けることができる
# 任意の型の戻り値をいくつでも0を含むいくつでも返すことができる
# 関数が明示的にreturnを呼び出さなければ、呼び出し元は戻り値としてはNoneを受け取る
def do_nothing():
    pass


print(do_nothing())
