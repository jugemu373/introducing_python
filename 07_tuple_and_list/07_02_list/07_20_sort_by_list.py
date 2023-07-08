# sort(), sorted()による要素の並べ替え
# sort()はリストのメソッドである。インプレースにリスト自体をソートする
# sorted()は組み込み関数である。ソートされたリストのコピーを返す
# リストの要素が数値なら、デフォルトで数値の昇順でソートする
# リストの要素が文字列ならアルファベット順でソートする
marxes = ['Groucho', 'Chico', 'Harpo']
sorted_marxes = sorted(marxes)
print(sorted_marxes)
print(marxes)

marxes.sort()
print(marxes)

# リストの要素が全て同じ型なら、sort()は正しく動作する
# 型が混ざっていてもいい場合がある
# 整数と浮動小数点数は、式の中ではPythonが自動的に変換を行う
numbers = [2, 1, 4.0, 3]
numbers.sort()
print(numbers)

# デフォルトのソート順は昇順だが、reverse=True引数を追加すると降順になる
numbers = [2, 1, 4.0, 3]
numbers.sort(reverse=True)
print(numbers)
