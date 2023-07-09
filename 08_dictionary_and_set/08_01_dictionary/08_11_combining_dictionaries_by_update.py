# update()は、辞書のキーとバリューを別の辞書にコピーできる
pythons = {
    'Chapman': 'Graham',
    'Cleese': 'Johe',
    'Gilliam': 'Terry',
    'Idle': 'Eric',
    'jones': 'Terry',
    'Palin': 'Michael',
}
print(pythons)

others = {
    'Marx': 'Groucho',
    'Howard': 'Moe',
}
print(others)

pythons.update(others)
print(pythons)


# 第2の辞書が第1の辞書に含まれているのと同じキーを持っている場合、第2の辞書のバリューが残る
first = {
    'a': 1,
    'b': 2
}
second = {
    'b': 'platypus',
}
first.update(second)
print(first)
