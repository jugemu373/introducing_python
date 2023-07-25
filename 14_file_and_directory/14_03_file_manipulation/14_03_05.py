# link(), symlink()によるリンク作成
"""
Unixでは、ファイルは1箇所にあっても複数の名前(リンク)を持つことができる。低水準のハードリンクでは、特定のファイルに対する
すべての名前を見つけるのは難しい。シンボリックリンクは自らのファイルとして新しい名前を格納する新しい方法で、オリジナルの名前と
新しい名前を同時に得ることができる。link()はハードリンク、symlink()は、シンボリックリンクを作る。
islink()は、ファイルがシンボリックリンクかどうかをチェックする。
"""
import os
os.link('oops.txt', 'yikes.txt')
print(os.path.isfile('yikes.txt'))
print(os.path.islink('yikes.txt'))

"新しいjeepers.txtから既存のoops.txtファイルへのシンボリックリンクは、次のようにして作る。"
os.symlink('oops.txt', 'jeepers.txt')
print(os.path.islink('jeepers.txt'))
