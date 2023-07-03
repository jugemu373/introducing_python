# strip()は引数が指定されていなければ、空白文字('', '\t', '\n')を取り除く
# strip()は先頭と末尾の両方でパディングを取り除く
# rstrip()末尾、lstrip()は先頭だけパディングを取り除く
world = "     earth  "
print(world.strip())
print(world.strip(' '))
print(world.lstrip())
print(world.rstrip())

# 引数で指定されたパディングがなければ何も起きない
print(world.strip('!'))

blurt = "What the...!!?"
blurt.strip('.?!')


import string
print(string.whitespace)
print(string.punctuation)
blurt = "What the...!!?"
print(blurt.strip(string.punctuation))
prospector = "What in tarnation ...??!!"
print(prospector.strip(string.whitespace + string.punctuation))
