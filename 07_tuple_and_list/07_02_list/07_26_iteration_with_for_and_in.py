# forとinによる反復処理
cheeses = ['brie', 'gjetost', 'havarti']
for cheese in cheeses:
    print(cheese)

# breakとcontinueを使ったfor文
cheeses = ['brie', 'gjetost', 'havarti']
for cheese in cheeses:
    if cheese.startswith('g'):
        print("I won't eat anything that starts with 'x'")
        break
    else:
        print(cheese)

# オプションelseも使うことができる
cheeses = ['brie', 'gjetost', 'havarti']
for cheese in cheeses:
    if cheese.startswith('g'):
        print("I won't eat anything that starts with 'x'")
        break
    else:
        print(cheese)
else:
    print("Didn't find anything that started with 'x")

# 最初のforが実行されない場合も、制御はelseに移る
cheeses = []
for cheese in cheeses:
    print('This shop has some lively', cheese)
    break
else:   # breakされなければチーズはない
    print('This is not much of a cheese shop, is it?')
