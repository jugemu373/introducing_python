"""
Pythonはカレントディレクトリからスタートしてこのディレクトリ名を探す。そして、choicesの中で、
advice.pyとfast.pyファイルを探す。
第1のモジュール(choices/fast.py)は、choicesディレクトリに移されただけで、先ほどと同じコードである。
"""

from choices import advice, fast

print("Let's go to", fast.pick())
print("Should we take out?", advice.give())
