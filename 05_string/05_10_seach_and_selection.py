poem = """All tha doth flow we cannot liquid name
Or else would ire and water be the same
But that is liquid which is moist and wet
Fire tha property can never get.
The 'tis not cod that doth the fire put out
But 'tis the wet that makes it die, no doubt."""

print(poem[:13])
print(len(poem))
print(poem.startswith('All'))
print(poem.endswith('That\'s all, folks!'))

# find()とindex()
# 文字列が見つからない場合、find()は-1を返す
# 文字列が見つかれない場合、index()は例外を投げる

# 最初に現れる"the"が現れるオフセットを探す
word = "the"
print(poem.find(word))
print(poem.index(word))

# 最後に"the"が現れるオフセットを探す
word = "the"
print(poem.rfind(word))
print(poem.rindex(word))

# 詩に含まれていない部分文字列を探すと以下のようになる
word = "duck"
print(poem.find(word))
print(poem.index(word))
print(poem.rfind(word))
print(poem.rindex(word))

# theという字のシーケンスは何個含まれているか
word = "the"
print(poem.count(word))

# 詩に含まれている文字は英数字だけか
print(poem.isalnum())
