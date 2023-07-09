# 辞書への要素を追加する
# キーを使って、バリューを参照し、バリューを代入する
# 辞書にキーが既にある場合には、既存のバリューが新しいバリューに置き換えられる
# キーがまだない場合は、バリューともども辞書に追加される

# リストと異なり、範囲外のインデックス(キー)を指定したために代入中に例外が送出される心配はない

pythons = {
    'chapman': 'Graham',
    'Cleese': 'John',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Palin': 'Michael'
}
print(pythons)

# Terry Gilliamを追加する
pythons['Gilliam'] = 'Gerry'
print(pythons)
pythons['Gilliam'] = 'Terry'
print(pythons)

# 辞書のキーは一意でなければならない
some_pythons = {
    'Graham': 'Chapman',
    'John': 'Cleese',
    'Eric': 'Idle',
    'Terry': 'Gilliam',
    'Michael': 'Palin',
    'Terry': 'Jones',
}
