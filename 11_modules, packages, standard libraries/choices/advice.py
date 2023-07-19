from random import choice


answers = [
    "Yes!"
    ,"No!"
    ,"Reply hazy"
    ,"Sorry, what?"
]

def give():
    """ランダムなアドバイスを返す"""
    return choice(answers)


"""
Pythonのバージョンが3.3よりも前の場合、choicesディレクトリをPythonパッケージにするためにしなければならないことがもう一つある。
__init__.pyという名前のファイルを入れなければならないのである。ファイルの内容は空でよい。しかし、3.3よりも前のバージョンでは、
ディレクトリをパッケージとして扱うためにこのファイルが必要になる。
"""