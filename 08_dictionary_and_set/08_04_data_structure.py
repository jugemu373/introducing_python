# 今まで取り上げてきたデータ構造
# リストは[]を使って作る
# タプルはカンマとオプションの()を使って作る
# 辞書と集合は{}を使って作る

# 集合以外では、[]を使って単一の要素にアクセスする
# リストとタプルの場合、[]の間にはオフセットを示す整数を入れる
# 辞書の場合はキーを入れる
# いづれの場合でも、返されるのは値、バリューである
# 集合の場合、あるかないかがわかるだけで、インデックスやキーはない
marx_list = ['Groucho', 'Chico', 'Harpo']
marx_tuple = ('Groucho', 'Chico', 'Harpo')
marx_dict = {'Groucho': 'banjo', 'Chico': 'piano', 'Harpo': 'harp'}
marx_set = {'Groucho', 'Chico', 'Harpo'}
print(marx_list[2])
print(marx_tuple[2])
print(marx_dict['Harpo'])
print('Harpo' in marx_list)
print('Harpo' in marx_tuple)
print('Harpo' in marx_dict)
print('Harpo' in marx_set)
