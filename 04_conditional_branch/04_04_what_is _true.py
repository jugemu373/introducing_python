# 以下は全てFalseとして扱われる
# ブール値: False
# 値の存在: None
# 整数の0: 0
# 浮動小数点数の0: 0.0
# 空文字列: ''
# 空リスト: []
# 空タプル: ()
# 空辞書: {}
# 空集合: set()
# これ以外の値はすべてTrueとしてみなされる

some_list = []
if some_list:
    print("There's something in here")
else:
    print("Hey, it's empty!")
