"""
ジェネレータ内包表記は、リスト、辞書、集合の内包表記と似ているが、[], {}ではなく、()で囲まれている
これは見えない形でyieldを実行し、ジェネレータオブジェクトを返すという点で、ジェネレータ関数の略記法のようでもある
"""

genobj = (pair for pair in zip(['a', 'b'], ['1', '2']))
print(genobj)

for thing in genobj:
    print(thing)
