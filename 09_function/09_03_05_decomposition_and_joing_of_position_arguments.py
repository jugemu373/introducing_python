# CやC++には*はポインタとして取り扱われる
# Pythonにはポインタはない
# 仮引数の一部として*を使うと、可変個の位置引数がタプルにまとめられてその仮引数にセットされるようになる
def print_args(*args):
    print('Positional tuple:', args)


print_args()
print_args(3, 2, 1, 'wait!', 'uh...')


def print_more(required1, required2, *args):
    print('Need this one:', required2)
    print('Need this one too:', required1)
    print('All the rest:', args)


print_more('cap', 'gloves', 'scarf', 'monocle', 'mustache wax')

# *を使うときにタプル引数をrgsと呼ぶ必要は特にない
# Pythonではタプルを使うのがイディオムとなっている
# 関数内の仮引数はparameterであり、*paramsと呼ぶべきだが、*argsと記述するのが一般的である

# 関数に位置実引数を渡すと、関数は渡された実引数を位置仮引数に対応付ける
# 関数にタプル実引数を渡すと、関数は渡されたタプル実引数をタプル仮引数に対応つける
# 関数に位置実引数を渡し、関数内でそれらを*args仮引数に「接合」できる
# *args仮引数は、タプルargsに解決される
# タプル実引数argsを関数内で仮引数*argsに「分解」させて関数内でタプル仮引数rgsに接合し直すことができる
print_args(2, 5, 7, 'x')
args = (2, 5, 7, 'x')
print_args(args)
print_args(*args)

# *構文が使えるのは、関数呼び出しと関数定義だけ
# *args
# SyntaxErrorをスロー

# 関数呼び出しの*argsはタプルrgsをカンマ区切りの位置仮引数に分解する
# 関数定義の*argsは、すべての位置実引数を単一のタプル仮引数argsに接合する
# *paramsやparamsという名前を使ってよいところだが、関数呼び出しでも*argsという名前を使う習慣である
