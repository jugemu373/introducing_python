# 文字列: Unicode
"""
Python3の文字列はバイトの配列ではなく、Unicode文字のシーケンスである。これはPython2と大きな違いである。

ASCII(American StandardCode for Information Interchange)は、マレットヘアが世界中で流行するよりも前の1960年第に定義されたものである。
当時のコンピュータは冷蔵庫の程の大きさで、計算が少しだけ特異なだけだった。

コンピュータの記憶の基本単位はバイトで、8個のビットを使って256種類の一意な値を表現できる。さまざまな値から、ASCIIは7ビットしか使っていない。
26種類の大文字、26種類の小文字、10種類の数字、いくつかの記号、いくつかの空白文字、そしていくつかの表示されない制御コードが含まれている。

世界にはASCIIで表現できる以上の文字がある。8ビットにもっと多くの文字と記号を詰め込むために、さまざまな試みがなされてきた。

・Latin-1 あるいはISO 8859-1
・Windowsコードページ1252

これらは8ビットをフルに使っているが、それでも十分ではないことがある。特にヨーロッパ以外の言語が必要になったときはそうである。
Unicodeは世界の言語のすべての文字と数学、その他の分野の記号(さらに絵文字)を定義しようと発展途上の国際標準である。

    Unicodeは、プラットフォーム、プログラム、言語に関わらず
    すべての文字に一意な番号を与える。
    -- Unicodeコンソーシアム

Unicodeのコード一覧ページには、現在定義されているすべてのキャラクタセットとそのイメージへのリンクが含まれている。最新バージョンは、
13万7千文字を超える文字、記号を定義しており、それぞれに一意な名前とID番号を与えている。Python3.8はこれらすべてを処理する。
文字は、面と呼ばれる8ビットセットに分割される。最初の256面は、基本多言語面(Basic Multilingual Plane)である。
"""