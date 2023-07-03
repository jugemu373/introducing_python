print(5.)
print(5.0)
print(05.0)

print(5e0)
print(5e1)
print(5.0e1)
print(5.0 * (10 ** 1))

million = 1_000_000.0
print(million)
print(1.0_0_0_1)

print(float(True))
print(float(False))

print(float(98))
print(float('99'))

print(float('98.6'))
print(float('-1.5'))
print(float('1.0e4'))

# 整数と浮動小数点数を混ぜて使うと、Pythonは自動的に整数値を浮動小数点数値にキャストする
# bool値も整数や浮動小数点数にキャストする
print(43 + 2.)
print(False + 0)
print(False + 0.0)
print(True + 0)
print(True + 0.)
