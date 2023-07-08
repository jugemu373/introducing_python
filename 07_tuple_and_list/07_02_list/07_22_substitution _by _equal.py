# =による代入
# 1つのリストを複数の変数に代入すると、その中の1つでリストを書き換えたときに、他のリストも書き換えられる
a = [1, 2, 3]
print(a)
b = a
print(b)
a[0] = 'surprise'
print(a)
print(b)

print(b)
b[0] = 'I hate surprises'
print(b)
print(a)
