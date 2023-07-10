# リスト、文字列、タプル、辞書から重複する値を取り除けば集合を作ることができる
print(set('letters'))

# リストから集合を生成
print(set(['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon']))

# タプルから集合を生成
print(set(('Ummgumma', 'Echoes', 'Atom Heart Mother')))

# set()に辞書に渡すと、キーだけが使われる
print(set({'apple': 'red', 'orenge': 'orenge', 'cherry': 'red'}))
