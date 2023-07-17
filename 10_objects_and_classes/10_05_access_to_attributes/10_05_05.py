# 属性を隠すための名前のマングリング
"""
これまでは、隠し属性にhidden_nameという名前をつけた。Pythonは、クラス定義の外からは見えないようにすべき属性の命名方法を持つ。
先頭に2つの__を付けるのである。
"""


class Duck:
    def __init__(self, input_name):
        self.__name = input_name

    @property
    def name(self):
        print('inside the getter')
        return self.__name

    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.__name = input_name


fowl = Duck('Howard')
print(fowl.name)
fowl.name = 'Donald'
print(fowl.name)


"__name属性には、アクセスできない。"
# print(fowl.__name) # AttributeErrorをスロー


"""
この命名方法を使っても、実際に属性が非公開になるわけではないが、Pythonは、外部コードが偶然当てたりしないようようなものになるように
名前をマングリング(変形する)。

マングリング後の属性へのアクセスは以下の通りである。
"""

print(fowl._Duck__name)

"""
inside the getterが表示されていない。
これは完全な保護とは言えないが、名前のマングリングは属性に対する意図せぬ(あるいは意図した)直接アクセスをある程度防ぐことはできる。
"""
