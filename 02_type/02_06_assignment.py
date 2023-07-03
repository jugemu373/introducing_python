x = 5
y = x + 12
print(y)


# 同時に複数の変数に値を代入できる
two = deux = zwet = 2
print(two, "/n")
print(deux, "/n")
print(zwet, "/n")


# 変数のコピー (mutableな型)
x = 5
print(x)
y = x
print(y)
x = 29
print(x)
print(y)


# 変数のコピー (immutableな型)
a = [2, 4, 6]
b = a
print(a)
print(b)
a[0] = 99
print(a)
print(b)