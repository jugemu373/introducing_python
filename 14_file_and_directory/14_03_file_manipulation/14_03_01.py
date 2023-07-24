# exists()によるファイルが存在することのチェック
"""
ファイルやディレクトリが本当にあるのか、あるような気がしているだけなのかを確かめるには、
次のように相対パスか絶対パスを引数として、exists()を呼び出せばよい。
"""
import os
print(os.path.exists('oops.txt'))
print(os.path.exists('./oops.'))
print(os.path.exists('waffles'))
print(os.path.exists('.'))
print(os.path.exists('..'))
