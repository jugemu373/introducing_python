# read()によるバイナリファイルの読み出し
"open()のモード引数を、'rb'で開く。"
fin = open('bfile', 'rb')
bdata = fin.read()
print(len(bdata))
bdata.close()
