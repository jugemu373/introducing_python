# HTMLエンティティ
# Python3.4以降では、Unicode文字列との間のエンコード、デコードの方法としてHTMLの文字エンティティが使えるようになった。
# ウェブを操作するときなどは特に、Unicode名から文字を探すよりもこちらの方が使いやすいだろう。
from html.entities import html5
import html
print(html.unescape("&egrave;"))

# このエンコード、デコードでは、10進または16進の数値エンティティも使える。
print(html.unescape("&#233;"))
print(html.unescape("&#xe9;"))

# 名前のエンティティの変換表を辞書としてインポートして自分で変換することもできる。
# エンティティの先頭の'&'を省略したものを辞書のキーとして使う。(末尾の';'も省略できるが、こちらは省略してもしなくても動作する。)
print(html5["egrave"])
print(html5["egrave;"])

# 反対方向の変換(Pythonが使っている1字のUnicode文字からHTML名への変換)では、まずord()で文字の10進を調べる。
char = '\u00e9'
dec_value = ord(char)
print(html.entities.codepoint2name[dec_value])

# 2字以上のUnicode文字列では、次のようなステップの変換を行う。
place = 'caf\u00e9'
byte_value = place.encode('ascii', 'xmlcharrefreplace')
print(byte_value)
print(byte_value.decode())

# place.encode('ascii', 'xmlcharrefreplace')はASCII文字を返すが、bytes型である(エンコードされているため)。
# byte_valueをHTML互換文字列に変換する為に次のbyte_value.decode()呼び出しが必要になる。
