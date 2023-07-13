# Pythonでは、すべてのものがオブジェクトである
# 関数は、Pythonでは第一級のオブジェクトである
# 変巣に関数を代入したり、ほかの関数の引数として関数を使ったり、関数から戻り値として関数を返したりできる

def answer():
    print(42)


answer()


def run_something(func):
    func()


run_something(answer)

# Pythonでは、()は関数呼び出しを意味する
# ()がなければ、Pythonは関数をほかのオブジェクトと同じように扱う
# Pythonでは他のすべてのものと同様に、関数もオブジェクトであるためである
print(type(run_something))


def add_args(arg1, arg2):
    print(arg1 + arg2)


print(type(add_args))

# func: 実行する関数
# arg1: funcの第1引数
# arg2: funcの第2引数
def run_something_with_args(func, args1, args2):
    func(args1, args2)


run_something_with_args(add_args, 5, 9)


def sum_args(*args):
    return sum(args)


def run_with_positional_args(func, *args):
    return func(*args)


run_with_positional_args(sum_args, 1, 2, 3, 4)

# 関数はイミュータブルなオブジェクトである
