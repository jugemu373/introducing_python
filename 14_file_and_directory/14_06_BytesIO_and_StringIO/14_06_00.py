# BytesIOとStringIO
"""
メモリ内のデータの書きかえ方や、ファイルデータの読み書きの方法はもう学んでいる。しかし、ファイルを対象とする関数を
呼び出してメモリ内にあるデータを操作したいとき(あるいはその逆)にはどのようにすればよいだろうか。一時ファイルを読み書きせずに
そのデータを書き換え、得られたバイト列や文字列を渡せるようにしたい。

このような場合、バイナリデータ(bytes)ならBytesIO、テキストデータ(str)ならStringIOが使える。これらを使うと、データは
ファイルライクオブジェクトにラップされ、この章で説明してきたファイル関数で操作できるようになる。

これらのクラスは、たとえばデータ形式の変換で役に立つ。イメージデータを読み書きするPILライブラリにこれを応用してみよう。
PILライブラリのImageオブジェクトのOpen()、save()の第1引数は、ファイル名かファイルライクオブジェクトである。
以下のコードは、メモリ内のデータの読み書きの為にBytesIOを使っている。このプログラムは、コマンドラインで指定された1個以上の
イメージファイルを読み出し、3つの異なる形式に変換してから、長さと出力の最初の10バイトを表示する。
"""
import sys
from io import BytesIO

from PIL import Image


def data_to_img(data):
    """メモリ内の<data>からPIL Imageオブジェクトを作って返す"""
    fp = BytesIO(data)
    return Image.open(fp)   # メモリから読み出し


def img_to_data(img, fmt=None):
    """PIL Imageオブジェクト<img>のイメージデータを<fmt>形式で返す"""
    fp = BytesIO()
    if not fmt:
        fmt = img.format    # もとの形式を維持
    img.save(fp, fmt)
    return fp.getvalue()


def convert_image(data, fmt=None):
    """イメージ<data>をPIL Imageオブジェクト経由で<fmt>形式に変換"""
    img = data_to_img(data)
    return img_to_data(img, fmt)


def get_file_data(name):
    for name in sys.argv[1:]:
        data = get_file_data(name)
        print("in", len(data), data[:10])
        for fmt in ("gif", "png", "jpeg"):
            out_data = convert_image(data, fmt)
            print("out", len(out_data), out_data[:10])

