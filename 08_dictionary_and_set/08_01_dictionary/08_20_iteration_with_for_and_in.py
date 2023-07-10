# 辞書(または辞書のkeys()関数)を反復処理すると、キーが返される
accusation = {
    'room': 'ballroom',
    'weapon': 'lead pipe',
    'person': 'Col Mustard',
}
for card in accusation:  # または、for card in accusation.keys()
    print(card)

# キーではなく、バリューを反復処理したいときには、辞書のvalues()関数を使う
for value in accusation.values():
    print(value)

# キーとバリューのタプルを反復処理したい場合には、辞書のitems()を使う
for item in accusation.items():
    print(item)

# items()で返してくる個々のタプルのうち第1の値(キー)をcard、第2の値(バリュー)をcontentsに代入したい
for card, contents in accusation.items():
    print('Card', card, 'has the contents', contents)
