# スライスによる要素の取り出し
# スライスを使うことによってリストのサブシーケンスを取り出すことができる
# リストのスライスもリストで返される
marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes[0:2])

# スライスは1以外のステップを指定できる
# 以下はリストを書き換えていない
print(marxes[::2])
print(marxes[::-2])
print(marxes[::-1])

# スライスは無効なインデックスを指定しても例外が発生しない。もっとも近い有効なインデックスに変身するか何も返さない
print(marxes[4:])
print(marxes[-6:])
print(marxes[-6:-2])
print(marxes[-6:-4])

# リストを直接逆順に書き換えるには、list.reverse()を使う
# revers()メソッドは、リストを書き換えるが値を返さない
marxes.reverse()
print(marxes)
