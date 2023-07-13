# 関数内関数は、クロージャとして機能する
# クロージャとは、他の関数によって動的に生成される関数で、自分の外で作られた変数の値を和えたり、覚えたりできる

def knights2(saying):
    def inner2():
        return f"We are the knights who say: '{saying}"
    return inner2


# 上の関数では、inner2を呼び出さない
# inner2は、クロージャの一種になっている

a = knights2('Duck')
b = knights2('Hasenpfeffer')

print(type(a))
print(type(b))

# これらは関数だが、クロージャでもある
a
b
a()
b()
