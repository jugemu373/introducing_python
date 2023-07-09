# clear()による全ての要素の削除

# pop()は、get()とdel文を組み合わせたような動作をする
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

del pythons['Marx']
print(pythons)
del pythons['Howard']
print(pythons)

print(len(pythons))
print(pythons.pop('Palin'))
# pop()でキーを削除した為、以下のコードはkeyErrorを送出する
# print(len(pythons))
# print(pythons.pop('Palin'))

print(pythons.pop('First', 'Hugo'))
print(len(pythons))

# clear()による全ての要素の削除
pythons.clear()
print(pythons)
pythons = {}
print(pythons)
