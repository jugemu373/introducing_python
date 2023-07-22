# エンコーディング
# 文字列をエンコードしてバイト列にする。文字列のencode()の第1引数は、エンコーディング名である。
# エンコーディング名 | 意味
# 'ascii' | 古き良き7ビットASCII
# 'utf-8' | 8ビット可変長エンコーディング。ほとんど必ずこれを使うことになる。
# 'latin-1' | ISO 8859-1と呼ばれているもの。
# 'cp-1252' | 一般的なWindowsエンコーディング。
# 'unicode-escape' | Python Unicodeリテラル形式。\uxxxxまたは\Uxxxxxxxx
# どんなものでもUTF-8にエンコードできる。
snow_man = '\u2603'
print(len(snow_man))
ds = snow_man.encode('utf-8')
print(len(ds))
print(ds)
# dsはbytes変数である。UTF-8以外のエンコーディングも使えるが、そのエンコーディングでUnicode文字列が処理できない場合はエラーが返される。
# 例えば、asciiエンコーディングを使うと、Unicode文字が有効なASCII文字になっている場合でなければエラーになる。

# ds = snow_man.encode('ascii')

# encode()は、エンコード例外を発生しにくくするための第2引数を持つ。デフォルト値は、今までの例のような動作をする'strict'で、
# ASCII以外の文字が使われているとUnicodeEncodeErrorを起こす。しかし、他の値も指定できる。'ignore'を使えば、エンコードできないものを捨ててしまう。
print(snow_man.encode('ascii', 'ignore'))
# 'replace'を使えば、エンコードできない文字を?に置き換える。
print(snow_man.encode('ascii', 'replace'))
# 'backslashreplace'を使えば、unicode-escape形式のPython Unicode文字列を生成する。
print(snow_man.encode('ascii', 'backslashreplace'))
# HTMLで安心して使える文字列を作りたい場合には、'xmlcharrefreplace'を使う。
print(snow_man.encode('ascii', 'xmlcharrefreplace'))
