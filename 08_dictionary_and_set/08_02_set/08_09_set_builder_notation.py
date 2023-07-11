# 集合内包表記
# 構文: { expression for expression in iterable }

# 集合内包表記もオプションのif節を使える
# 構文: { expression for expression in iterable if condition }
a_set = {number for number in range(1, 6) if number % 3 == 1}
print(a_set)
