count = 1
# 3行目の条件を満たす限り、同じ処理を繰り返す
while count <= 5:
    print(count)
    # ループを繰り返すごとに変数countをインクリメントする
    count += 1


# break文による中断
# 何かが起こるまでループを続けたいが、それがいつ起こるかわからない場合はbreak文を持つ、無限ループが使える
# input()を使いキーボードから入力行を読み出し、最初の文字を大文字に変換して入力行を表示する
# qだけの行を読み込んだらループを終了する
while True:
    stuff = input("String to capitalize [type q to quit]:")
    if stuff == "q":
        break
    print(stuff.capitalize())


# continue文による次のイテレーションの開始
# continue文を使うことでループを抜け出さずに次のイテレーション(反復処理の1回分)を始ることができる
while True:
    value = input("Integer , please [q to quit]: ")
    if value == 'q':   # 終了
        break
    number = int(value)
    if number % 2 == 0: # 偶数の場合
        continue
    print(number, "squared is", number * number)


# else文によるbreakのチェック
# whileループがbreakをせずに終了し場合、制御はオプションのelse節に渡される
# 何かをチェックするためにwhileループを書き、それが見つかったらすぐにbreakするときにこれを使う
# else節はwhileループが終了したものの、探し物が見つからなかったときに実行される
numbers = [1, 3, 5]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print('Found even number', number)
        break
    position += 1
else:   # breakしていない
    print('No even number found')
