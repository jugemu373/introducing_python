# []による文字の抽出
# 文字列の中の1つの文字を取り出したいときには、文字列変数名の後ろに[]で囲んだ文字のオフセットを添える
# オフセットは先頭から0で始まり、末尾の文字は-1で指定できる
letters = 'abcdefghijklmnopqrstuvwxyz'
letters[0]
letters[1]
letters[-1]
letters[-2]
letters[25]
letters[5]
# 文字列の長さ以上のオフセットを指定すると、IndexErrorをスローする
# letter[100]

# 文字列はイミュータブルであるため、文字列に直接文字を挿入したり、指定したインデックの文字を書き換えたりすることはできない
# 'Henny'を'Penny'に書き換えようとした場合、TypeErrorをスローする
# name = 'Henny'
# name[0] = 'P'
# 代わりに、replace()などの文字列メソッドやスライスの組み合わせを使う必要がある
name = 'Henny'
name.replace('H', 'P')
print(name)
print('P' + name[1:])


# スライスによる部分文字列の取り出し
# スライスを使えば、文字列から部分文字列(文字列の一部)を取り出すことができる
# スライスは、[]と先頭オフセット(start)、末尾オフセット(end)、ステップ(step)で定義する
# [:]は、先頭から末尾までのシーケンス全体を抽出する
# [start:]は、startオフセットあら末尾までのシーケンスを抽出する
# [:end]は、先頭からend -1オフセットまでのシーケンスを抽出する
# [start:end:step]は、step文字ごとにstartオフセットからend -1オフセットまでのシーケンスを抽出する

letters = 'abcdefghijklmnopqrstuvwxyz'
letters[:]
letters[20:]
letters[10:]
letters[12:15]
letters[-3:]
letters[18:-3]
letters[-6:-2]
letters[::7]
letters[4:20:3]
letters[19::4]
letters[:21:5]
letters[-1::-1]
letters[::-1]
letters[-50:]
letters[-51:-50]
letters[70:71]
