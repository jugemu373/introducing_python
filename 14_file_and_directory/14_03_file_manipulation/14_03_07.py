# chown()によるオーナーの変更
"""
この関数もUnix/Linux/Mac専用で、数値でユーザID(uid), グループID(gid)を指定すれば、ファイルのオーナー、
グループ所有権を変更できる。
"""
import os
uid = 5
gid = 22
os.chown('oops.txt')
