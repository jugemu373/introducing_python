# 直接アクセル
"""
属性の値は直接、設定するこごができる。
"""


class Duck:
    def __init__(self, input_name):
        self.name = input_name


fowl = Duck('Daffy')
print(fowl.name)


"しかし、誰かが悪さをしたらどうなるだろうか"
fowl.name = 'Daphne'
print(fowl.name)
