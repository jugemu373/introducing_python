# パターンの特殊文字
"""
正規表現の説明の多くは、いきなり正規表現の定義方法の詳細から始まってしまうことが多い。
正規表現は、一度に細部を全て頭に叩きこめるほど小規模な技術ではない。正規表現は非常に多くの記号を使っている。

match(), search(), findall(), sub()の動作をしっかりと理解してから、正規表現を組み立てるための詳細に踏み込んで行く。
作ったパターンは、これらすべての関数で使うことができる。

既に基礎的なものはコード例で使っている。

・特殊文字でないすべての文字は対応するリテラルにマッチする。
・.は、\n以外の任意の1文字にマッチする。
・*は、任意の個数(0を含む)をの直前の文字にマッチする。
・?は、0個か1個の直前の文字にマッチする(直前の文字がオプション扱いになる)。

特殊文字一覧
パターン | マッチ
\d | 1個の数字
\D | 1個の数字以外の文字
\w | 1個のUnicode単語文字(または英数字と_)
\W | 1個のUnicode単語文字(または英数字と_)以外の文字
\s | 1個の空白文字
\S | 1個の空白以外の文字
\b | 単語の境界(\wと\Wの間。順序はどちらでもよい)
\B | 単語の境界以外の文字間

Pythonのstringモジュールは、テストのための文字列定数を予め定義している。
"""
import string
import re

printable = string.printable
print(len(printable))
print(printable[0:50])
print(printable[50:])

"printableの数字を抽出する。"
print(re.findall(r'\d', printable))

"printableの中でUnicode単語文字を抽出する(_が含まれる)"
print(re.findall('\w', printable))

"printableの空白文字を抽出する。"
print(re.findall('\s', printable))
"""
これらは順にスペース、タブ、改行、復帰、垂直タブ、フォームフィードを表す。
正規表現はASCIIだけに制御されているわけではない。\dは、ASCIIの'0'~'9'だけでなく、Unicodeが数字と呼んでいるらゆるものにマッチする。
FileFormat.infoからASCIIに含まれない2個の小文字を追加してみよう。

・3個のASCII英字
・\wにマッチしない記号
・UnicodeのLATIN SMALL LETTER E WITH CIRCUMFLEX(\u00ea)
・UnicodeのLATIN SMALL LETTER E WITH BREVE(\u0115)
"""
x = 'abc' + '-/*' + '\u00ea' + '\u0115'
print(re.findall(r'\w', x))
