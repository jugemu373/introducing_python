# Python3のUnicode文字列
# """
# 文字のUnicode IDか名前を知っていれば、Python文字列でそれを使うことができる。


# ・\uの後ろに4個の16進数字を続けたものは、256の基本多言語面のどれかに含まれる文字に対応する。最初の2桁は面番号(00~FF)、
# 後半の2桁はその面の中での文字のインデックスをあらわす。面00はASCIIであり、面内での文字の位置もASCIIと同じになっている。

# ・上位面の文字は、基本多言語面の文字よりも多くのビットを必要とする。これらの文字のためのPythonのエスケープシーケンスは、
# \uの後ろに8個の16進数を続けたものである。左端の数字は0でなければならない。

# ・すべての文字について、\ N{name}を使えば、標準の名前で1つの文字を指定できる。名前のリストは、Unicode文字名牽引にまとめられている。


# Pythonのunicodedataモジュールには、双方向ンの変換関数が含まれている。

#     lookup()
#         名前(大文字と小文字を区別しない)を与えると、Unicode文字が返される。
    
#     name()
#         Unicode文字を与えると、大文字の名前が返される。
    
# Unicode文字を引数とするテスト関数を記述する。
# """
import unicodedata
def unicode_test(value):
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print(f'value="{value}", name="{name}", value2="{value2}"')

unicode_test('A')
unicode_test('$')
unicode_test('\u00a2')
unicode_test('\u20ac')

# このテストで問題になりそうなことは、テキストの表示に使っているフォントだけだ。すべてのUnicode文字のイメージを持つフォントは
# ほとんどないに等しく、イメージのない文字に対してはそのことを表す代替記号を表示する。
unicode_test('\u2603')

# Pythonの文字列にcaféという単語を保存する場合
place = 'café'
print(place)

# テキストの為にUTF-8エンコーディングを使っているソースからコピーアンドペースしたため、エラーにならず表示することができた。
print(unicodedata.name('\u00e9'))
print(unicodedata.lookup('LATIN SMALL LETTER E WITH ACUTE'))

# これでコードか名前によって文字列caféを指定できるようになった。
place = 'caf\u00e9'
print(place)
place = 'caf\N{LATIN SMALL LETTER E WITH ACUTE}'
print(place)

# 文字列にéを直接挿入していたが、文字を追加して文字列を組み立てて行くこともできる
u_umlaut = '\N{LATIN SMALL LETTER E WITH ACUTE}'
print(u_umlaut)
drink = 'Gew' + u_umlaut + 'rztraminer'
print('Now I can finally have my', drink, 'in a', place)

# len()に文字列を渡すと、バイト数ではなく、Unicodeの文字数を数える。
print(len('$'))

# Unicode文字の数値IDがわかっていれば、標準のold()、chr()を使って整数IDとUnicode文字の1字を簡単に相互変換できる。
print(chr(233))
print(chr(0xe9))
print(chr(0x1fc6))
