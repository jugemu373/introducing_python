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
