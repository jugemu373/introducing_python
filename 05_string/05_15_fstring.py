# f文字列はPython3.6から追加
# 先頭のクォートの前に'f'か'F'を入れる
# {}で変数名か式を囲み、その値を文字列に差し込む

import string

thing = 'wereduck'
place = 'werepond'
print(f'The {thing} is in the {place}')
print(f'The {thing.capitalize()} is in the {place.rjust(20)}')


# f文字列は : の後にパディング、配置、符号、幅、文字数 / 精度を指定できる
print(f'The {thing:>20} si in the {place:.^20}')


# Python3.8以降では、変数の値だけではなく名前も表示したいときにサポートしている
print(f'{thing =}, {place =}')

# 式にも使うことができる
print(f'{thing[-4:] =}, {place.title() =}')

# =の後ろに : を続ければ、配置、幅などの書式指定をすることもできる
print(f'{thing = :>4.4}')

