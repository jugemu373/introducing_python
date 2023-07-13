# The Zen of Pythonは、「読みやすさは大切だ」と言っている
# docstringとは、関数本体の先頭に文字列を組み込めば、関数定義にドキュメントを付けられる

def echo(anything):
    """echoは、与えられた入力引数を返す"""
    return anything


def print_if_true(thing, check):
    """
    第2引数が真なら、第1引数を表示する
    処理内容:
        1. 第2引数が真かどうかをチェックする
        2. 真なら第1引数を表示する
    """
    if check:
        print(thing)


# 関数のdocstringは、Pythonのhelp()を呼び出せば表示される
# 引数として関数名を渡すと、引数リストともに、きれいに整形されたdocstringが返される
help(echo)
print(echo.__doc__)


# __ダブルアンダースコア(Pythonの世界でダンダーと呼ばれている)は、プログラムが自分の変数名を使わないだろうという理由から
# Pythonの内部変数の名前の一部としてさまざまな場所で使われている
