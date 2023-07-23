# カレンダーとクロック
"""
プログラマたちは、日付と時刻に驚くほどの労力を捧げている。彼らがぶつかる問題について少し説明したから、
状況を少しなりともすっきりさせるベストプラクティスとトリックを紹介する。

日付はさまざまな方法で表現できる。実際に、方法が多すぎるのだ。英語のグレゴリオ暦でも、単純な日付の書き方が以下のようにいくつかある。

    Jury 21 1987
    21 Jul 1987
    21/7/1987
    7/21/1987

特に問題になるのは、日付の表現が曖昧になる場合があることである。上の例では、7月21日であるとすればすぐにわかる。
21月はありえないからである。しかし、1/6/2012ではどうだろうか。これは1月6日なのか、6月1日なのかは判断できない。

月名は、グレゴリオ暦を採用している国の言語の間でもまちまちだ。年と月でさえ、文化が異なれば定義が異なることがある。

時刻には時刻特有の厄介な問題がある。特に大きいのは各地の標準時間帯の違いとサマータイムの問題である。
標準時間帯の地図を見ると、標準時間帯は経度が15度(360度/24)ずれるごとに変わるのではなく、政治的歴史的な理由で境界線が引かれていることが分かる。
そして、サマータイムの開始日と終了日は国によってまちまちだ。それだけにとどまらず、南半球の国々が時計を進めるごとに、北半球の国々は時計を戻し、
逆も行われる。なぜそうなのかは少し考えればわかるだろう。

Pythonの標準ライブラリには、datetime, time, calendarなど、日付と時刻のモジュールが多数含まれている。
重なり合う機能を持つものもあり、すこし紛らわしい。
"""