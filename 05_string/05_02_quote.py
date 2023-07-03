print('snap')
print("Crackle")
# シングルクォート、ダブルクォートに違いはない

# 先頭がfまたはFを用いた'f文字列': フォーマット済文字列
# 先頭がrまたはRを用いた'raw文字列': 文字列内のエスケープシーケンスがエスケープシーケンスとして解釈されないようにする
# 先頭がfrまたはFR,Fr,fRを用いた文字列は上記を組み合わせたもの
# 先頭がuのものはUnicode文字列: 普通の文字列と変わらない
# 先頭がbのものはbytes型のバイト文字列

print("'Nay!' said the naysayer. 'Neigh?' said the horse")
print('The rare double quote in captivity: ".')
print('A "two by four" is actually 1 1/2" × 3 1/2".')
print("'There's the man that shot my paw!' cried the limping hound.")


# 3つのシングルクォートやダブルクォートを使うこともできる
# 複数行文字列を作るために使われる
'''Boom!'''
"""Eek!"""

poem = """There was a Young Lady f Norway,
Who casually sat in a doorway;
When the door squeezed her flat,
She exclaimed "What of that?"
This courageous Young Lady of Norway."""

# トリプルクォートを使わずに上の変巣を作ろうとするとPythonは２行目に進んだところで例外が発生する
# poem = 'There was a young lady of Norway,

poem2 = """I do not like thee, Doctor Fell.
    The reason why, I cannot tell.
    But this I know, and know full well:
    I do not like thee, Doctor Fell.
"""
print(poem2)
# print()と対話型インタプリタの自動エコーの出力には違いがある
# 対話型インタプリンタの場合
# I do not like thee, Doctor Fell.\n    The reason why, I cannot tell.\n    But this I know, and know full well:\n  I do not like thee, Doctor Fell.


# print()は文字列から先頭と末尾のクォートを取り除き、文字列の内容を表示する
# 表示する項目の間にスペースを追加し、末尾に改行を追加する
print('Give', "us", """some""", """space""")


# 空文字列
empty_string1 = ''
empty_string2 = ""
empty_string3 = ''''''
empty_string4 = """"""


# str()関数
str(98.6)
str(1.0e4)
str(True)

