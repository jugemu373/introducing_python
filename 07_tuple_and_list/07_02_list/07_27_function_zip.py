# zip()による複数のシーケンスの反復処理
# zip()を使えば、複数のシーケンスを並行して反復処理できる
# zip()は、もっとも短いシーケンスの用を処理し尽くしたときに止まる
days = ['Monday', 'Tuesday', 'wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ise cream', 'pie', 'pudding']
for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day, ":drink", drink, "- eat", fruit, "- enjoy", dessert)

# 複数のシーケンスをたどって、オフセットが共通する要素からタプルを作ることができる
english = 'Monday', 'Tuesday', 'Wednesday'
french = 'lundi', 'mardi', 'mercredi'
print(list(zip(english, french)))
# zip()の結果を直接dict()に渡すと、英仏辞書ができあがる
print(dict(zip(english, french)))
