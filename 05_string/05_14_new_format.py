# 新しいスタイルのフォーマットは、format_string.format(data)
# 先頭に : を入れる
# オプションのパディング文字(デフォルトは'')。文字列の幅が下限値よりも短いときにパディングのために使われる
# オプションの配置(align)文字。新しいスタイルでは左揃えがデフォルトになるが'<'でも左揃えになる。'>'で右揃え、'^'で中央揃えになる。
# オプションの数値の符号(sign)。何も指定しないと、負数にマイナス記号(-)を付け、正数はそのまま出力する。' 'を指定すると、負数にマイナス記号、:
# 正数にスペースを付けて出力する。'+'を指定すると、負数にマイナス記号、正数にプラス記号(+)を付けて出力する。
# オプションの幅の下限。
# オプションの文字数の上限 / 精度。これを指定するときには幅の下限と文字数の上限を区別するために、文字数の上限の前に.を入れる。
# 変換型。

thing = 'woodchuck'
print('{}'.format(thing))

# format()への引数は、書式指定文字列内の{}というプレースホルダ－(位置を指定するための記号)の順序と同じでなければならない
thing = 'woodchuck'
place = 'lake'
print('The {} is in the {}.'.format(thing, place))

# 引数の位置を指定することができる
print('The {1} is in the {0}.'.format(place, thing))

# format()にはキーワード引数を渡すことができる
print('The {thing} is in the {place}.'.format(thing='duck', place='bathtub'))

# 辞書型のデータも扱うことができる
d = {'thing': 'duck', 'place': 'bathtub'}
print('The {0[thing]} is in the {0[place]}.'.format(d))


thing = 'wraith'
place = 'window'
print('The {} is at the {}'.format(thing, place))
print('The {:10s} is at the {:10}'.format(thing, place))
print('The {:<10s} is at the {:<10s}'.format(thing, place))
print('The {:^10s} is at the {:^10s}'.format(thing, place))
print('The {:>10s} is at the {:>10s}'.format(thing, place))
print('The {:!^10s} is at the {:!^10s}'.format(thing, place))
