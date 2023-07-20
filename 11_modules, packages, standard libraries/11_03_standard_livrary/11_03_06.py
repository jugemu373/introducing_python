# pprint()によるきれいな表示
from pprint import pprint
from collections import OrderedDict

quotes = OrderedDict([
    ('Moe', 'A wise guy, huh?'),
    ('Larry', 'Ow!'),
    ('Curly', 'Nyuk nyuk!'),
])

"print()は、続けて表示するだけである。"
print(quotes)

"pprint()は、読みやすくするために要素の位置を揃えようとする。"
pprint(quotes)
