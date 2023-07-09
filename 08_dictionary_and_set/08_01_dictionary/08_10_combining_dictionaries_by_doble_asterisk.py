# Python3.5以降、**を使った新しい辞書の方法が追加された
first = {
    'a': 'agony',
    'b': 'bliss',
}
second = {
    'b': 'bagels',
    'c': 'candy',
}
print({**first, **second})

# 実際には、3つ以上の辞書を渡せる
third = {
    'd': 'donuts'
}
print({**first, **second, **third})

# 実態ではなく参照をコピーする浅いコピーである
# 元の辞書との関係のない新しい辞書を作りたい場合には、deepcopy()を使う
