# insert()によるオフセットを指定した要素の追加
# insert()は、オフセットを指定し、その前に要素を追加する
# 末尾を超えるオフセットを指定した場合は、append()と同じ動きをとる
marxes = ['Groucho', 'Chico', 'Harpo']
marxes.insert(2, 'Gummo')
print(marxes)
marxes.insert(10, 'Zeppo')
print(marxes)
