# Pythonのラムダ関数は、1つの文で表現される無名関数である
# 小さな通常の関数の代わりに使える
# ラムダは0個以上のカンマ区切りの実引数を取り、その後ろに:を付け、さらに関数定義が続く
# ラムダを使わなければ、小さな関数をいくつも作ってその名前を覚えておかなければならない
# 特に、GUIでコールバック関数を定義するときにラムダが役に立つ

"""
words: 単語のリスト
func: words内の個々の単語に適用される関数
"""


def edit_story(words, func):
    for word in words:
        print(func(word))


# この関数を試すには、単語のリストと個々の単語に適用される関数が必要である
stairs = ['thud', 'meow', 'thud', 'hiss']


def enliven(word):
    return word.capitalize() + '!'


edit_story(stairs, enliven)


edit_story(stairs, lambda word: word.capitalize() + '!')
