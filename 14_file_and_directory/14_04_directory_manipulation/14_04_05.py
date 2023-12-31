# glob()によるパターンにマッチするファイルのリストの作成
"""
glob()は、Unixシェルの規則を使って、ファイル、ディレクトリ名のパターンマッチを行う。より包括的な正規表現を使うわけではない。
規則をまとめると以下のようになる。

    * はすべてのものにマッチする(正規表現なら .* と表記する)
    ? は任意の1字にマッチする。
    [abc]は、a, b, cのいづれかにマッチする。
    [!abc]は、a, b, c以外の文字にマッチする。
"""
import glob
"mで始まるファイル、ディレクトリのリストを作る。"
print(glob.glob('m*'))

"中身はなんであれ、2文字の名前を持つファイル、ディレクトリのリストを作る。"
print(glob.glob('??'))

"mで始まりeで終わる8文字のファイル名を返すリストを作る。"
print(glob.glob('m??????e'))

"k, l, mのどれかで始まりeで終わるファイル。"
print(glob.glob('[klm]*e'))
