"""
ソースコードを書き換えずに既存の関数に変更を加えたい場合がある。よく知られているのは、
引数として何が渡されたかを見るためのデバッグ文の追加など
デコレータは、入力として関数を1つ鳥、別の関数を返す関数である。
"""


def document_it(func):
    """document_it()は、次のことを行うデコレータである
    ・関数名と実引数の値を表示する
    ・その実引数を渡して関数を実行する
    ・結果を表示する
    ・実際に使うために変更後の関数を返す
    """
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function


"""
document_it()にどんなfuncを渡しても、document_it()が追加した文を含む新しい関数が返される
デコレータは、funcのコードを一切実行しなくてもよいのだが、document_it()は途中でfuncを呼び出し、
追加のコードの結果とともにfuncの結果も得られるようにしている
"""


def add_ints(a, b):
    return a + b


add_ints(3, 5)

cooler_add_ints = document_it(add_ints)
cooler_add_ints(3, 5)


"""
手作業でデコレータの戻り値を代入しなくても、デコレートしたい関数の直前に
@decorator_nameを追加すれば変更後の動作が得られる
"""


@document_it
def add_ints(a, b):
    return a + b


add_ints(3, 5)


# 関数に対するデコレータは複数持てる。結果を自乗するsquare_it()という別のデコレータを書いてみよう
def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return new_function


"""
関数にもっとも近いデコレータが先に実行され、次にその上のデコレータが実行される。
土の順番でも最終的な結果は同じだが、中間の手順が変わる
"""


@document_it
@square_it
def add_ints(a, b):
    return a + b


add_ints(3, 5)


@square_it
@document_it
def add_ints(a, b):
    return a + b


add_ints(3, 5)
