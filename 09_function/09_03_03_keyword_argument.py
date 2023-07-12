# キーワード引数
# 対応する仮引数の名前を指定して実引数を渡せばよい
# 関数定義と引数の順序が異なっていてもかまわない

def menu(wine, entree, dessert):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}


print(menu(entree='beef', dessert='bagel', wine='bordeaux'))

# 位置引数とキーワード引数は併用可
print(menu('frontenac', dessert='flan', entree='fish'))
