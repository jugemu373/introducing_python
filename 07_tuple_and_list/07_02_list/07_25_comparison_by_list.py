# リストの比較
# リストは、==, < などの比較演算子で直接比較できる
# 両方のリストをたどり、同じオフセットの要素を比較する
# リストaがリストよりも短く、ある要素がすべて等しければaはbよりも「小さい」と判断される
a = [7, 2]
b = [7, 2, 9]
a == b
a <= b
a < b
