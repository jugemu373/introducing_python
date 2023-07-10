# 辞書内包表記
# 構文: {key_expression: value_expression for expression in iterable}
word = 'letters'
letter_counts = {letter: word.count(letter) for letter in word}
print(letter_counts)

# 上記のコードをパイソニックに書き換えたコード
word = 'letters'
letter_counts = {letter: word.count(letter) for letter in set(word)}
print(letter_counts)


# 辞書内包表記もif節と複数のfor節を使うことができる
# 構文: {key_expression: value_expression for expression in iterable if condition}
vowels = 'aeiou'
word = 'onomatopeia'
vowel_counts = {letter: word.count(letter)
                for letter in set(word) if letter in vowels}
print(vowel_counts)
