# pathlibの使い方
"""
Python3.4でpathlibが追加された。os.pathモジュールに変わって使うべきものとして位置づけられている。
しかし、なぜ新しいモジュールが必要なのか。

pathlibは、ファイルシステムのパス名を文字列として扱うのではなく、Pathオブジェクトというものを導入して文字列よりも高水準なものとして扱う。
Path()でPathオブジェクトを作ってから、文字としての'/'ではなく、演算子の/でパスを組み立てる。
"""
from pathlib import Path, PureWindowsPath
file_path = Path('eek') / 'urk' / 'snort.txt'
print(file_path)

"""
このスラッシュを使った操作は、Pythonの特殊メソッドを利用したものである。
Pathには、自分についての情報を返すメソッドである。
"""
print(file_path.name)
print(file_path.suffix)
print(file_path.stem)

"""
file_pathは、ファイル名、パス名文字列と同じようにopen()に渡せる # Python3.6以降からである。
"""
PureWindowsPath(file_path)
print(PureWindowsPath(file_path))
