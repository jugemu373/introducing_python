# 関数を呼び出すためには、関数名と()を入力する
def do_nothing():
    pass


do_nothing()


# 1個の単語を入力する関数の定義
def make_a_sound():
    print('quack')


make_a_sound()


# 引数がないが、値を返す関数の定義
def agree():
    return True


# 関数を呼び出した上でifを使えば、戻り値をテストできる
if agree():
    print('Splendid!')
else:
    print('That was unexpected.')
