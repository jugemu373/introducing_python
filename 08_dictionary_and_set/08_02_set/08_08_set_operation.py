# 積集合演算子&
drinks = {
    'martini': {'vodka', 'vermouth'},
    'black russian': {'vodka', 'kahlua'},
    'white russian': {'cream', 'kahlua', 'vodka'},
    'manhattan': {'rye', 'vermouth' 'bitters'},
    'screwdriver': {'orange juice', 'vodka'},
}
for name, contents in drinks.items():
    if contents & {'vermouth', 'orange juice'}:
        print(name)

# &演算子の結果は、比較している両方の集合に含まれているすべての要素を格納する集合である
for name, contents in drinks.items():
    if 'vodka' in contents and not contents & {'vermouth', 'cream'}:
        print(name)

bruss = drinks['black russian']
wruss = drinks['white russian']

a = {1, 2}
b = {2, 3}

# intersection()メソッドを使えば、積集合が得られる
print(a & b)
print(a.intersection(b))

print(bruss & wruss)

# |演算子か集合のunion()を使って和集合を得られる
print(a | b)
print(a.union(b))

# 差集合(集合Aには含まれているものの、集合Bには含まれていない要素)
# -記号か集合のdifference()で得られる
print(a - b)
print(a.difference(b))
print(bruss - wruss)
print(wruss - bruss)

# 対称差(排他的論理和)は、^か集合のsymmetric_difference()を使う
print(a ^ b)
print(a.symmetric_difference(b))
print(bruss ^ wruss)

# <= か集合のissubset()を使えば、片方の集合がもう片方の集合の部分集合になっているかのチェックできる
print(a <= b)
print(a.issubset(b))
print(bruss <= wruss)
print(a <= a)
print(a.issubset(a))

# 集合Aが集合Bの真部分集合となるためには、集合Bが集合Aのすべての要素に加えて別の要素を持っていなければない
# 真部分集合関係は、<で計算できる
print(a < b)
print(a < a)
print(bruss < wruss)

# 上位集合(スーパーセット)は部分集合の逆で、集合Bのすべての要素が集合Aの要素にもなっている関係のこと
# 上位集合かどうかは、>=演算子か集合のissuperset()で調べることができる
print(a >= b)
print(a.issuperset(b))
print(wruss >= bruss)

# すべての集合は、自分自身の上位集合である
print(a >= a)

# >演算子を使えば、集合Aか集合Bの真上位集合(集合Aに集合Bのすべての要素とその他の要素が含まれている)かどうかがわかる
print(a > b)
print(wruss > bruss)

# 集合は自分自身の真上位集合にはならない
print(a > a)
