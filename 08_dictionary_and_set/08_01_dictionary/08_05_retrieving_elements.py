# 辞書とキーを指定して、対応するバリューを取り出し
some_pythons = {
    'Graham': 'Chapman',
    'John': 'Cleese',
    'Eric': 'Idle',
    'Terry': 'Gilliam',
    'Michael': 'Palin',
    'Terry': 'Jones',
}
print(some_pythons['John'])

# キーが辞書になければ、例外が発生する
# print(some_pythons['Groucho'])

print('Groucho' in some_pythons)


# get()メソッドは、辞書、キー、オプションのバリューを指定しキーがあればそのバリューが返される
print(some_pythons.get('John'))
print(some_pythons.get('Groucho', 'Not a Python'))
print(some_pythons.get('Groucho'))
