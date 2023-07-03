# \(バックスラッシュ)は継続文字。行末に/を置くとPythonはまだ改行していないものとして処理を行う。

total = 0
total += 1
total += 2
total += 3
total += 4
print(total)

total = 1 + \
total = 2 + \
total = 3 + \
total = 4
print(total)

# 以下はSyntaxErrorをスローする。
total = 1 +

# ()パレンシスで囲うとエラーを出さない。
total = (
    1 +
    2 +
    3 +
    4
)
print(total)

