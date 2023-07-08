# pop()でオフセットを指定して要素を取り出し、削除する方法
# pop()はリストから要素を取り出し、同時にリストからその要素を削除できる
# オフセットを指定してpop()を呼び出すと、そのオフセットの要素が返される
# 引数を指定しない場合、デフォルトで-1が渡される
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print(marxes.pop())
print(marxes)
print(marxes.pop(1))
print(marxes)
