disaster = True
if disaster:
    print("Woe!")
else:
    print("Whee!")
# 変数disasterにブール値Trueを代入
# ifとelseを使って条件分岐を行い、disasterの値によって異なるコードを実行
# テキストを表示するために、print()関数を呼び出し


# ネストした条件分岐
furry = True
large = True
if furry:
    if large:
        print("It's a yeti")
    else:
        print("It's a cat!")
else:
    if large:
        print("It's a Whale!")
    else:
        print("It's a human. Or a hairless cat.")


# elif(else ifの意)を使った条件分岐
color = "mauve"
if color == "red":
    print("It's a tomato.")
elif color == "green":
    print("It's a green pepper.")
elif color == "bee purple":
    print("I don't know what it is, but only bees can see it.")
else:
    print("I've never heard of the color", color)


# Pythonの比較演算子
# 等しい: ==
# 等しくない: !=
# 未満: <
# 以下: <=
# より大きい: >
# 以上: >=

# 比較演算子の挙動確認
x = 7
print(x == 5)
print(x == 7)
print(5 < x)
print(x < 10)

# 論理演算子: and, or, notは比較対象の要素よりも優先順位が低い
# 比較対象となる部分が先に計算されてからブール演算が行われる
print(5 < x and x < 10)

# 優先順位を明確にする場合、()を使う
print((5 < x) and (x < 10))

# 論理演算を組み合わせた比較
print(5 < x or x < 10)
print(5 < x and x > 10)
print(5 < x and not x > 10)

# 複数の比較をandでする場合、Pythonでは次のように書くことができる
print(5 < x < 10)
print(5 < x < 10 < 999)