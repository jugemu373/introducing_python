# イテレータとは、イテレーションごとにリスト、辞書などから要素を1つずつ取り出して返すもの
# 反復処理を実行するためには反復する対象が必要
# イテラブル(list, tuple, dictなどのミュータブルなデータ型: 反復可能なオブジェクト)
word = 'thud'
offset = 0
while offset < len(word):
    print(word[offset])
    offset += 1

for letter in word:
    print(letter)


# break文による中断
for letter in word:
    if letter == 'u':
        break
    print(letter)


# continue文による次のイテレーションの開始
numbers = [1, 2, 3, 4, 5, 6]
for number in numbers:
    if number == 3:
        continue
    print(number)


# else節によるbreak文のチェック
# whileと同様でbreakが呼び出されなければ、else節が実行される
for letter in word:
    if letter == 'x':
        print("Eek! An 'x'!")
        break
    print(letter)
else:
    print("No 'x' in there.")

