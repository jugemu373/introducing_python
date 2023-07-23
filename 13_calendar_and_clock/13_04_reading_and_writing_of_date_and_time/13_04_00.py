# 日時の読み書き
"""
timeモジュールのctimeは、Unix時間を文字列に変換する。
"""
import locale
from datetime import time
from datetime import date
import time
now = time.time()
print(time.ctime(now))

"""
日時データは、strftime()でも文字列に変換できる。strftime()は、datetime、date、timeオブジェクトのメソッド、
timeモジュールの関数として提供されている。

strftime()の書式指定子
書式指定子  :   日時の単位  :   範囲
%Y          :   年          :   1900-...
%m          :   月          :   01-12
%B          :   月名        :   January, ...
%b          :   月略称      :   Jan, ...
%d          :   日          :   01-31
%A          :   曜日        :   Sunday, ...
%a          :   曜日略称    :   Sun, ...
%H          :   時間(24時間) :  00-23
$I          :   時間(12時間) :  01-12
%p          :   AM/PM       :   AM, PM
%M          :   分          :   00-59
%S          :   秒          :   00-59
数値は0埋めされる
"""
"""
timeモジュールのstrftime()で、struct_timeオブジェクトを文字列に変換する。
"""
fmt = "It's %A, %B %d, %Y, local time %I:%M:%S%p"
t = time.localtime()
print(t)
print(time.strftime(fmt, t))

"""
dateオブジェクトでこれを試すと、日時の部分だけが整形され、時刻の部分はデフォルトで深夜(24時間制の0時0分)になる。
"""
some_day = date(2019, 7, 4)
print(some_day.strftime(fmt))

"timeオブジェクトを使うと、時刻の部分だけが変換される"
# some_time = time(10, 35)
# print(some_time.strftime(fmt))

"""
timeオブジェクトの日付の部分は全く意味がないので、使いたいと思わないだろう。
逆に文字列を日時情報に変換するには、同じ書式指定文字列とともにstrptime()を使う。
正規表現によるパターンマッチには使われない。書式指定子以外の部分(%でない部分)は、
正確に一致していなければならない。2012-01-29のように、「年-月-日」という形の書式を指定してみよう。
解析したい文字列がダッシュではなくスペースを使った場合、以下のようになる。
"""
fmt = "%Y-%m-%d"
# print(time.strptime("2019-01-29", fmt)) # ValueError: 日時データ'2019 01 29'はフォーマット'%Y-%m-%d'に一致しない。

"ダッシュ付きの文字列を渡してみる。"
print(time.strptime("2019-01-29", fmt))

"日時文字列にマッチするようにfmt文字列の方を変えればよい。"
fmt = "%Y %m %d"
print(time.strptime("2019 01 29", fmt))

"""
文字列が書式指定に合っているように見えても、値が範囲外だと例外が送出される。
"""

"""
名前はロケール、すなわちOSの国際設定、地域設定によって変わる。月や曜日の表示方法を変えなければならない時には、
setlocale()を使ってロケールを変更する。setlocale()の第1引数は日時のロケールを設定することを示すlocale.LC_TIME、
第2引数は言語と国の略称を組み合わせた文字列である。ハロウィンパーティに海外出身の友人を招待するケースを考える。
月名と日、曜日をアメリカ英語。フランス語、ドイツ語、スペイン語、アイスランド語で表示する。
"""
halloween = date(2019, 10, 31)
for lang_country in ['en_us', 'fr_fr', 'de_de', 'es_es', 'is_is']:
    locale.setlocale(locale.LC_TIME, lang_country)
    print(halloween.strftime('%A, %B, %d'))


"次のコードを試せば、lang_countryという値の文字列を得ることができる。"
names = locale.locale_alias.keys()
print(names)


"""
namesから、setlocale()で動作しそうなロケール名だけを取り出してみる。
2文字の言語コードの後ろに_が続き、更に2文字の国別コードが続くものである。
"""
good_names = [name for name in names if len(name) == 5 and name[2]]
print(good_names)

"最初の5個はどのようなものだろうか。"
print(good_names[:5])

de = [name for name in good_names if name.startswith('de')]
print(de)


"""
set_locale()を実行して、次のようにそのロケールは使っているOSでサポートされていないというエラーが返された場合、
    
    locale.Error: unsupported locale setting

OSに何を追加すべきかを明らかにしなければなない。Pythonが有効なロケールと言ったとしても、このエラーが起こる場合がある。
macOSでcy_gb(イギリスのウェールズ語)というロケールを試したときにこのエラーが起きる。それでも、先ほどのis_is(アイスランドのアイスランド語)
は受け付けられたみたいだが。
"""
