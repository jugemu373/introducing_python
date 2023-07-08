# スライスによる要素の書き換え
numbers = [1, 3, 3, 4]
numbers[1:3] = [8, 9]
print(numbers)

# リストに代入する右辺の要素は、左辺のスライスと要素数が等しくなくても構わない
numbers = [1, 3, 3, 4]
numbers[1:3] = [7, 8, 9]
print(numbers)

numbers = [1, 3, 3, 4]
numbers[1:3] = []
print(numbers)

# 代入式の右辺はリストでなくてもよい
# Pythonのイテラブルなら、分割されてリスト要素に代入される
numbers = [1, 3, 3, 4]
numbers[1:3] = (98, 99, 100)
print(numbers)

numbers = [1, 3, 3, 4]
numbers[1:3] = 'what'
print(numbers)
