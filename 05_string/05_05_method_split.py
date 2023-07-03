# split()はstrクラスに属するメソッド
# セパレータに基づいて文字を分割し、文字列のリストを作る
# 構文: string.function(arguments)
tasks = 'get gloves, get mask, give cat vitamins, call ambulance'
print(tasks.split(','))
# 空白文字をセパレータとして扱う
print(tasks.split())
