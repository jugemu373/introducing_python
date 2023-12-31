# オブジェクトとその他のものの使い分けの方法
"""
コードをクラス、モジュール、それ以外のもののどれにまとめるべきかを決めるためのガイドラインを示す。

・動作(メソッド)は同じだが、内部状態(属性)は異なる複数のインスタンスを必要とするときには、オブジェクトがもっとも役に立つ。

・クラスは継承をサポートするが、モジュールはサポートしない。

・何かを1つだけ必要とするときには、モジュールがよい。Pythonモジュールは、プログラムに何度参照されても、1個のコピーしかロードされない。
(Java, C++プログラマ向けに言えば、Pythonモジュールはシングルトンとして使える)

・複数の値を持つ変数があり、これらを複数の関数に引数として渡せるときには、それをクラスとして定義した方がよい場合がある。
例えば、カラーイメージを表現するために、size, colorなどのキーを持つ辞書を使っていたとする。プログラム内のカラーイメージごとに
別々の辞書を作り、それをscale(), transform()などの関数に引数として渡してもよいのだが、キーやかんすうが増えていくと煩雑になっていく。
それよりも、size, colorなどの属性を持ち、scale(), transform()などのメソッドを持つImageクラスを定義した方がすっきりする。
こうすれば、カラーイメージの為のすべてのデータ、メソッドを1か所で定義できる。

・問題にとってもっとも単純な方法を使う。辞書、リスト、タプルは、モジュールよりも単純で小さく高速であり、モジュールはクラスよりも普通は単純だ。
    グイドのアドバイス：
        データ構造を作りこみすぎないようにしよう。オブジェクトよりもタプルの方がよい(名前つきタプルも試してみよう)。ゲッター/セッター関数よりも単純な
        フィールドを選ぶようにしよう。組み込みデータ型はプログラマの友達だ。数値、文字列、タプル、リスト、集合、辞書をもっと使おう。そして、
        コレクションライブラリ、特にdequeをチェックしよう。

・データクラスという新しい選択肢がある。
"""