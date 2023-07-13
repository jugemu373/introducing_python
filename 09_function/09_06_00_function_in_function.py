# 関数を他の関数の中で定義できる
# 関数内関数は、関数内で複数回実行される複雑な処理を実行したいときに役立つ
# ループやコードの重複を避けることができる

def outer(a, b):
    def inner(c, d):
        return c + d
    return inner(a, b)


outer(4, 7)


def knights(saying):
    def inner(quote):
        return f"We are knights who say: '{quote}'"
    return inner(saying)


knights('Ni!')
