# パターン: メタ文字
"""
メタ文字一覧
パターン : マッチ対象
abc : リテラルのABC
( expr ) : expr
expr1 | expr2 : expr1 または expr2
. : \n以外の任意の文字
^ : ソース文字列の先頭
$ : ソース文字列の末尾
prev? : 0か1個のprev
prev* : 0個以上のprev(欲張り)
prev*? : 0個以上のprev(控えめ) 
prev+ : 1個以上のprev(欲張り)
prev+? : 1個以上のprev(控えめ)
prev{m} : m個の連続したprev
prev{m, n} : m個以上n個未満の連続したprev(欲張り)
prev{m, n}? : m個以上n個未満の連続したprev(控えめ)
[ abc ] : aまたはbまたはc(a | b | cと同じ)
[^abc] : aまたはbまたはc以外
prev(?=next) : nextが続いているprev
prev(?!next) : nextが続いていないprev
(?<=prev) : prevが前にあるnext
(?<!prev) : prevが前にないnext
"""
import re
source = """I wish I may, I wish I might
Have a dish of fish tonight"""
"任意の位置にあるwishを探す。"
print(re.findall(r'wish', source))
"任意の位置にあるwishかfishを探す。"
print(re.findall(r'wish|fish', source))
"先頭でwishを探す"
print(re.findall(r'^wish', source))
"先頭でI wishを探す"
print(re.findall(r'^I wish', source))
"末尾でfishを探す"
print(re.findall(r'fish$', source))
"末尾でfish tonightを探す"
print(re.findall(r'fish tonight.$', source))
"""
^と$は、アンカーと呼ばれている。
^は探索をソース文字列の先頭に固定し、$はソース文字列の末尾に固定する。.$は、行末の任意の文字(ピリオドを含む)にマッチする。
より正確にリテラルにマッチさせるには、ドットをエスケープすべきである(ドットの前にエスケープ文字の\を置く)。
"""
print(re.findall(r'fish tonight\.$', source))
"wかfのあとにishが続いているものを探す"
print(re.findall(r'[wf]ish', source))
"w, s, hのどれかが1個以上続いているところを探す"
print(re.findall('[wsh]+', source))
"ghtの後ろに英数字以外のものが続いているところを探す"
print(re.findall(r'ght\W', source))
"I(Iとスペース)の後ろにwishが続くところを探す"
print(re.findall(r'I (?=wish)', source))
"wishの前にI(Iとスペース)があるところを探す"
print(re.findall(r'(?<=I) wish', source))
"""
正規表現のパターンの規則とPythonの文字列の規則が矛盾を起こすことが時々ある。
以下の文は先頭がfishになっている単語にマッチするはずだ。
"""
print(re.findall('\bfish', source))
"しかし、マッチすることはない"
"""
Pythonは文字列のために少数のエスケープ文字を使っている。例えば\bは文字列ではバックスペースという意味になるが、正規表現のミニ言語では
単語の境界という意味になる。正規表現文字列を定義するときには、誤ってPython文字列のエスケープ文字という矛盾を起こすのを避けるために、
raw文字列と呼ばれるものを使う。正規表現をパターン文字列を定義するときに、必ずその前にrの文字を追加するようにすればよい。
そうすれば、以下のようにPythonのエスケープ文字は無効になる。
"""
print(re.findall(r'\bfish', source))
