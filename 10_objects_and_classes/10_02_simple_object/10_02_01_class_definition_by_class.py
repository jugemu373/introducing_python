"""
今まで誰も作ったことのない新しいオブジェクトを作るときには、オブジェクトの内容を規定するクラスを作らなければならない。
オブジェクトは箱に例えられる場合がある。クラスは、そのような箱を作るための鋳型のようなものである。Pythonは、例えば
'cat'や'duck'などの文字列オブジェクトや、リスト、辞書などの標準データ型を作るための組み込みクラスを持つ。
Pythonでカスタムオブジェクトを作るためには、まずclassキーワードを使ってクラスを定義しなけらばならない。
"""
# 空クラスを定義
class Cat:
    pass


# オブジェクトは、関数と同じようにクラス名を呼び出して作る
a_cat = Cat()
another_cat = Cat()


"""
Cat()呼び出しは、Catクラスから2個のオブジェクトを作り、a_catとanother_catに代入している。しかし、Catクラスは
空なので、そこから作ったオブジェクトはただ存在するだけでほとんど何もできない。とはいえ、少しできることもある。
"""
