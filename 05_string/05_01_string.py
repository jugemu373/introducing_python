# 文字列はPythonシーケンス(列、連なり)の一つ
# Pythonの文字列はイミュータブルである
# 文字列をその場で書き換えることはできない
# 文字列の一部を別の文字列にコピーして同じ結果を得ることはできる


# \によるエスケープ
# \n = 改行
palindrome = 'A man,\n plan,\nA canal:\nPanama.'
print(palindrome)

# \t = タブ文字
print('\tabc')
print('\ttbc')
print('ab\tc')
print('abc\t')

testimony = "\"I did nothing!\" he said. \"Or that other thing.\""
testimony # 対話型インタプリンタ
print(testimony)

speech = 'The backslash (\\) bends over backwards to please you.'
print(speech)


# raw文字列ではエスケープを扱えない
info = r'Type a \n to get a new line in a normal string'
info # 対話型インタプリンタ
print(info)

# raw文字列でも本物の('\nではない')改行は取り消されない
poem = r"""Boys and girls, come out to play.
The moon doth shine as bright as day."""
poem # 対話型インタプリンタ
print(poem)


# +演算子を使うことにより、リテラル文字列、文字列変数を連結できる
'Release the kraken! ' + 'No, wait!' # 対話型インタプリンタ

# テラル文字列の場合は順に並べるだけでも連結できる(文字列変数はできない)
"My word! " "A gentleman caller!"
"Alas! " "The kraken!"

# ()で囲めば行末の改行をエスケープしなくて済む
vowels = ( 'a'
         "e" """i"""
         'o' """u"""
         )
vowels # 対話型インタプリンタ

# 文字列の連結では、自動的にスペースを追加しない
# print()関数の各引数の間にはPythonが自動でスペースを挿入し、末尾に改行を追加する
a = 'Duck.'
b = a
c = 'Grey Duck!'
a + b + c # 対話型インタプリンタ
print(a, b, c)


# *による繰り返し
# *演算子を使うと、文字列を繰り返すことができる
start = 'Na ' * 4 + '\n'
middle = 'hey ' *3 + '\n'
end = 'Goodbye.'
print(start + start + middle + end)



