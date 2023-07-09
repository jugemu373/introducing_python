# dict()を使わない辞書の生成
acme_customer = {
    'first': 'Wile',
    'middle': 'E',
    'last': 'Coyote'
}
print(acme_customer)

# dict()に名前付き引数と値を渡す方法
acme_customer = dict(first="Wile", middle="E", last="Coyote")
print(acme_customer)

# dict()に名前付き引数と値を渡す際には、引数名が変数名として正しくなければならない(スペースなし、予約語なし)
# x = dict(name="Elmer", def="hunter")
# print(x)
