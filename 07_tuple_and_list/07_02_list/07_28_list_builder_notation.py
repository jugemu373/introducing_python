# リスト内包表記による作成
# リストは、リスト内法表記でも生成できる
# 1から5までの整数のリストは、次のように一度に1つずつ要素を追加すれば作れる
number_list = []
number_list.append(1)
number_list.append(2)
number_list.append(3)
number_list.append(4)
number_list.append(5)
print(number_list)

# 反復子とrange()で生成
number_list = []
for number in range(1, 6):
    number_list.append(number)
print(number_list)

# range()の出力を直接リストに変換しても作れる
number_list = list(range(1, 6))
print(number_list)

# パフォーマンスを求める場合、リスト内法表記を使うケースがある
# 構文: [expression for item in iterable]
number_list = [number for number in range(1, 6)]
print(number_list)
number_list = [number -1 for number in range(1, 6)]
print(number_list)

# リスト内法表記には条件式も追加できる
# 構文: [expression for item in iterable if condition]
a_list = [number for number in range(1, 6) if number % 2 == 1]
print(a_list)
a_list = []
for number in range(1, 6):
    if number % 2 == 1:
        a_list.append(number)
print(a_list)

# リスト内法表記はネストにできる
rows = range(1, 4)
cols = range(1, 3)
for row in rows:
    for col in cols:
        print(row, col)

rows = range(1, 4)
cols = range(1, 3)
cells = [(row, col) for row in rows for col in cols]
for cell in cells:
    print(cell)

# タプルのアンパックを使って、cellsリストを反復処理しながらタプルからrow, colの値を抜き出すことができる
for row, col in cells:
    print(row, col)
