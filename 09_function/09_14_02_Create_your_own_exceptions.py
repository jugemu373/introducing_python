"""
IndexErrorなどはPythonがその標準ライブラリで定義済みのものであった。
これらの例外は、自分の目的で自由に使うことができる。

また、自分のプログラムの中で発生することのある特殊な状況に対処するために
独自の例外型を定義することもできる。
"""

"""
クラスを使って新しいオブジェクト型を定義する必要がある。
"""

"""
例外はクラスであり、Exceptionクラスの子クラスである。
クラスUppercaseExceptionを作り、文字列に大文字の単語が含まれていたら
生成されるようにしてみる。
"""

class UppercaseException(Exception):
    pass


words = ['eenie', 'meenie', 'miny', 'MO']
for word in words:
    if word.isupper():
        raise UppercaseException(word)


"""
raise文は式として与えられた例外か現在のスコープで最終的に有効となる例外を送出する文である。
ここでは、UppercaseExceptionのふるまいさえ定義していない。
例外が送出されたときに何を表示すべきかも、親クラスのExceptionに任せている。

例外オブジェクト自体にアクセスして、情報を表示することもできる。
"""

# try:
#     raise OopsException('panic')
# except OopsException as exc:
#     print(exc)
