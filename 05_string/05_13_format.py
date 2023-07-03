# 3種類のスタイルでフォーマットすることができる

# Python2、3でサポート
# 形式: format_string % data
# データ型一覧
# %s = 文字列
# %d = 10進整数
# %x = 16進整数
# %o = 8進整数
# %f = 10進浮動小数点数
# %e = 指数形式浮動小数点数
# %g = 10進または指数形式浮動小数点数
# %$ = リテラルの%

# 指定できる値一覧
# 先頭の'%'文字
# オプションの配置文字: 指定なしか'+'なら右添え、'-'なら左添え(中央揃えは指定できない)
# オプションのフィールド幅の下限
# オプションで幅下限と文字数上限を区切る'.'
# オプションの文字数の上限。変換型がsなら、値のうちの何文字を出力するか、変換型がfなら精度(小数点以下何桁まで出力するか)を示す
# 上記、変換型

# %sは任意のデータ型で使え、スペースを加えたりせずに文字列にフォーマットする
# 整数の場合
print('%s' % 42)
print('%d' % 42)
print('%x' % 42)
print('%o' % 42)

# 浮動小数点数の場合
print('%s' % 7.03)
print('%f' % 7.03)
print('%e' % 7.03)
print('%g' % 7.03)

# 整数とリテラルの%の場合
print('%d%%' % 100)

# 文字列と整数の挿入
actor = 'Richard Gere'
cat = 'Chester'
weight = 28
print("My wife's favorite actor is %s" % actor)
print("Our cat %s weights %s ponds" % (cat, weight))

# %sの場合
thing = 'woodchuck'
print('%s' % thing)
print('%12s' % thing)
print('%+12s' % thing)
print('%-12s' % thing)
print('%.3s' % thing)
print('%+12.3s' % thing)
print('%-12.3s' % thing)

# %fの場合
thing = 98.6
print('%f' % thing)
print('%12f' % thing)
print('%+12f' % thing)
print('%-12f' % thing)
print('%.3f' % thing)
print('%12.3f' % thing)
print('%-12.3f' % thing)

# %dの場合
thing = 9876
print('%d' % thing)
print('%12d' % thing)
print('%+12d' % thing)
print('%-12d' % thing)
print('%.3d' % thing)
print('%12.3d' % thing)
print('%-12.3d' % thing)
