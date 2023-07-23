# datetimeモジュール
"""
標準ライブラリのdatetimeモジュールは、日時データを処理する。このモジュールは4個のメインオブジェクトクラスを定義しており、
それぞれ多数のメソッドを抱えている。

・年月日を対象とする        date
・時分秒と端数を対象とする  time
・日付と時刻の両方を対象とする  datetime
・日付と自国の感覚を対象とする  timedelta

dateオブジェクトは、年月日を指定すれば作ることができる。これらの値は属性として取り出すことができる。
"""
from datetime import datetime
from datetime import time
from datetime import timedelta
from datetime import date
halloween = date(2019, 10, 31)
print(halloween)
print(halloween.day)
print(halloween.month)
print(halloween.year)

"dateの内容は、isoformat()で表示できる。"
print(halloween.isoformat())

"""
isoというのは、日時表現の国際標準であるISO 8601の事である。これに従うと、もっとも広い部分からもっとも狭い部分に向かって数字を並べていくことになる。
この形式だとまず年、次に月、次に日になるので、ソートも正しくなる。プログラムで日付を表現するときやデータを保存するために日付付きファイル名を使う
時には、たいていこの形式を選ぶ。日付の解析、書式設定でもっと複雑なことができる。strptime()、strftime()については、すぐあとで説明する。

以下のコード例では、today()を使って今日の日付を生成している。
"""
now = date.today()
print(now)

"以下のコード例は、timedeltaオブジェクトを使ってdateの1日後、17日後、1日前を計算する。"
one_day = timedelta(days=1)
tomorrow = now + one_day
print(tomorrow)
print(now + 17 * one_day)
yesterday = now - one_day
print(yesterday)

"""
dateの範囲は、date.min(1年1月1日)からdate.max(9999年12月31日)までだ。そのため、原始時代の日付や天文学的な時間の計算ではdateは使い物にならない。

datetimeモジュールのtimeオブジェクトは、1日の中の時刻を表現する。
"""
noon = time(12, 0, 0)
print(noon)
print(noon.hour)
print(noon.minute)
print(noon.second)
print(noon.microsecond)

"""
引数は、もっとも大きな単位(時)からもっとも小さな単位(マイクロ秒)に向かって並べる。一部の引数を指定していない場合、timeはその部分をゼロと判断する。
なお、マイクロ秒単位まで保存、取得できるからといって、コンピュータからマイクロ秒まで正確に時刻を読み取れるわけでない。秒以下の計測値の精度は、
ハードウェアとオペレーティングシステムのさまざまな要素によって左右される。

datetimeオブジェクトは、日付と自国の両方を含む。例えば、次のようにすれば、datetimeは直接作ることができる。
"""
some_day = datetime(2019, 1, 2, 3, 4, 5, 6)
print(some_day)

print(some_day.isoformat())

"""
datetimeオブジェクトにも、isoformat()がある。
表示されている中央のTは日付と時刻を分割している。
datetimeは、現在の日付と時刻を取得するnow()を持つ。
"""
now = datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)

"""
combine()を使えば、dateオブジェクトとtimeオブジェクトを結合してdatetimeオブジェクトを作ることができる。
"""
noon = time(12)
this_day = date.today()
noon_today = datetime.combine(this_day, noon)
print(noon_today)

"逆にdate()、time()を使えば、datetimeからdate、timeを抽出できる。"
print(noon_today.date())
print(noon_today.time())
