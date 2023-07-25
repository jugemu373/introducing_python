# os.path.join()によるパス名の組み立て
"""
os.path.join()を使えば、パスセパレータでディレクトリ名とファイル名をつなぎ合わせて長いパス名を作れる。
"""
import os
win_file = os.path.join('eek', 'urk')
win_file2 = os.path.join(win_file, 'snort.txt')

"MacやLinuxでこのコードを実行すると以下のようなパス名を得ることができる。"
print(win_file)

"Windowsで同じコードを実行すると、以下のようなパス名が得られる。"
print(win_file)

"""
しかし、どこで実行されるかによって同じコードが別の結果を生み出すのはまずいだろう。
新しいpathlibモジュールは、この問題に対してポータブルなソリューションを提供する。
"""
