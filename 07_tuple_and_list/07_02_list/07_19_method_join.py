# join()による文字列への変換
# join()メソッドは文字列のメソッドである
# join()はsplit()の逆である
marxes = ['Groucho', 'Chico', 'Harpo']
print(', '.join(marxes))

friends = ['Harry', 'Hermione', 'Ron']
separator = ' * '
joined = separator.join(friends)
print(joined)
separated = joined.split(separator)
print(separated)
separated == friends
