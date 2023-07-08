# extend()または+=によるリストの結合
# extend()を使えば、他のリストを1つにまとめることができる
marxes = ['Groucho', 'Chico', 'Harpo']
others = ['Gummo', 'Zeppo']
marxes.extend(others)
print(marxes)


# + や +=でも連結することができる
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes += others
print(marxes)


# append()を使うとothersの要素を追加するのではなく、othersを1つの要素として追加する
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes.append(others)
print(marxes)
