setup = 'a duck goes into a bar...'
print(setup.strip('.'))

# 文字列はイミュータブルであるため、メソッドを使った加工は書き換えている訳ではなく、新しい文字列を生成している


# 先頭の単語の先頭文字を大文字に変換
print(setup.capitalize())

# 全ての単語の先頭文字を大文字に変換(タイトルケース)
print(setup.title())

# 全ての文字を大文字に変換
print(setup.upper())

# 全ての文字を小文字に変換
print(setup.lower)

# 大文字小文字を反転
print(setup.swapcase())
