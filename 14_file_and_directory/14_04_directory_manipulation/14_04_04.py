# chdir()によるカレントディレクトリの変更
"chdir()を使えば、別のディレクトリに移動することができる。"
import os
os.chdir('poems')
with os.scandir('poems') as it:
    entries = [entry.name for entry in it]

print(entries)
