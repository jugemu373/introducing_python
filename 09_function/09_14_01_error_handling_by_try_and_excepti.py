"""
成り行きに任せるのではなく、tryを使って例外が発生しそうな場所を囲み、
exceptを使って例外処理を提供するべきだ。
"""
short_list = [1, 2, 3]
position = 5
try:
    short_list[position]
except:
    print('Need a position between 9 and', len(
        short_list) - 1, 'but got', position)


"""
引数なしのexceptを指定すると、あらゆる例外がキャッチされる。
しかい、複数の例外が発生する可能性がある時には、それぞれの為に別々の例外ハンドラを用意した方がいい。
しかし、これは強制ではない。ただのexceptを使ってすべての例外をキャッチすることはできるが、
その処理はおそらく通りいっぺんの役に立たないものになるだろう。専用例外ハンドラはいくつも指定できる。

例外について型だけでなく、詳細情報がわかるようにしたい場合がある。
次のようにすれば、name変数に完全な例外オブジェクトを格納できる。

except exceptiontype as name
"""


short_list = [1, 2, 3]
while True:
    value = input('position [q to quit]? ')
    if value == 'q':
        break
    try:
        position = int(value)
        print(short_list[position])
    except IndexError as err:
        print('Bad index:', position)
    except Exception as other:
        print('Something else broke:', other)
