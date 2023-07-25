# rmdir()による削除
"rmdir()は、ディレクトリを削除する。"
import os
os.rmdir('poem')
print(os.path.exists('poem'))
