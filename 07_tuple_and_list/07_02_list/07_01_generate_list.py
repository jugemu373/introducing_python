# リストは、要素を順番に管理したいとき、順序と内容が変わる場合があるときに向いている
# リストは、ミュータブルである
# リストの内容は直接変更できる
# 新しい要素を追加したり、既存の要素を削除、置換したりできる
# リスト内では同じ値が複数回登場してもよい

# []による生成
# リストは、0個以上の要素をそれぞれカンマで区切り、全体を[]ブラケットで囲んで作る
empty_list = []
weekdays = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'saturday', 'sunday']
big_birds = ['emu', 'ostrich', 'cassowary']
first_names = ['Graham', 'John', 'Terry', 'Michael', 'Eric']
leap_years = [2000, 2004, 2008]
randomness = ['Punxsatawney', {"groundhog": "Phil"}, "Feb. 2"]

print(empty_list)
print(weekdays)
print(big_birds)
print(first_names)
print(leap_years)
print(randomness)
