# replace()は文字列の一部を置換できる
setup = "a duck goes into a bar..."
print(setup.replace('duck', 'marmoset'))
print(setup)

# 以下はマッチした文字列を最大で100回置換する
print(setup.replace('a', 'a famous', 100))
