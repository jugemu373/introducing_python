# 正規化
# Unicode文字の中には、複数のUnicodeエンコーディングを持つものがある。それらのエンコーディングはどれも同じように見えるが、
# 使われているバイトシーケンスが異なるので、比較したときに同じ文字と評価されない。
import unicodedata
eacute1 = 'é'       # UTF-8、ペーストしたもの
eacute2 = '\u00e9'  # Unicodeコードポイント
eacute3 = '\N{LATIN SMALL LETTER E WITH ACUTE}'
eacute4 = chr(233)
eacute5 = chr(0xe9)
print(eacute1, eacute2, eacute3, eacute4, eacute5)
print(eacute1 == eacute2 == eacute3 == eacute4 == eacute5)
import unicodedata
print(unicodedata.name(eacute1))
print(ord(eacute1)) # 10進整数に変換
print(0xe9)         # Unicodeの16進整数値

# 次に、eアクサンテギュを追加してアクセント付きのeを作る
eacute_combined1 = "e\u0301"
eacute_combined2 = "e\N{COMBING ACUTE ACCENT}"
eacute_combined3 = "e" + "\u0301"
print(eacute_combined1, eacute_combined2, eacute_combined3)
print(eacute_combined1 == eacute_combined2 == eacute_combined3)
print(len(eacute_combined1))

# ここでは2つの文字から1つのUnicode文字を組み立てており、先ほどの'é'と同じように見えるが、実は違う。
print(eacute1 == eacute_combined1)

# 異なるソースから入手した2つの異なるUnicode文字列があるとき、片方がeacute1、もう片方がeacute_combined1を使っていれば
# 両者は同じように見えるが、不思議と同じものとして扱われないことが起きる。
# この問題は、unicodedataモジュールのnormalize()を使えば解決できる。
eacute_normalized = unicodedata.normalize('NFS', eacute_combined1)
print(len(eacute_normalized))
print(eacute_normalized == eacute1)
print(unicodedata.name(eacute_normalized))

# NFCは正規化形式C(Normalization Form C)の略である。
