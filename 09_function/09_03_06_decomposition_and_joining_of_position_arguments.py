# **を使えば、キーワード引数を1個の辞書にまとめることができる
# 引数の名前は辞書のキー、引数の値は辞書のバリューになる
def print_kwargs(**kwargs):
    print('keyword arguments:', kwargs)


print_kwargs()
print_kwargs(wine='merlot', entree='mutton', dessert='macaroon')

# 関数内部では、kwargsは辞書である
# 実引数は、下の順序で並べる
# 必須位置引数
# オプション位置引数(*args)
# オプションキーワード引数(**args)

# **構文が使えるのは、巻子呼び出しと関数定義だけである
# Python3.5以降では、{**a, **b}という形の辞書でも使わるようになった

# 関数にキーワード実引数を渡すと、関数は渡された実引数をキーワード仮引数に対応付ける
# 関数に辞書実引数を渡すと、関数は渡された辞書実引数を辞書仮引数に対応つける
# 関数に1個以上のキーワード引数(name=Value)を渡し、関数内でそれらを**kwargs仮引数に「接合できる」
# **kwargs仮引数は、辞書kwargsに解決される
# 関数呼び出しの**kwargsは辞書kwargsをname=Value引数に分解させる
# 関数定義の**kwargsは、すべてのname=Value実引数を単一の辞書仮引数kwargsに接合する
