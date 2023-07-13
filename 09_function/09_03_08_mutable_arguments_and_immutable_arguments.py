# 文字列や数値はイミュータブル
# リストや辞書はミュータブル
# 実引数がミュータブルなら、関数内で対応する仮引数を介して書き換えられる可能性がある

outside = ['one', 'fine', 'day']


def mangle(arg):
    arg[1] = 'terrible!'


# 以下のようにリスト内の値が書き換えられてしまう
print(outside)
print(mangle(outside))
print(outside)
