# keysを使えば、辞書のすべてのキーを取得できる
signals = {
    'green': 'go',
    'yellow': 'go faster',
    'red': 'smile for the camera',
}
print(signals.keys())

# Python2では、keys()はリストを返す
# Python3では、イテラブルなキーのビューであるdict_keys()を返す
# リストで返すためには、list()を呼び出す必要がある
print(list(signals.keys))
