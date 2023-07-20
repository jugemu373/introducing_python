# スタック+キュー==デック
"""
deque(デック)は、両端キューのことで、スタックとキューの両方の機能を持つ。シーケンスのどちらの橋でも要素を追加、削除できるようにしたい
ときに便利だ。popleft()は、デックから左端の要素を削除して返す。pop()は右端の要素を削除して返す。
これらを組み合わせれば、両端から中央に向かって文字を1つずつ処理できる。両端の文字が等しければ、中央に到達するまでの文字の削除を続けていく。
"""
from collections import deque


def palindrome(word):
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
        return True


print(palindrome('a'))
print(palindrome('racecar'))
print(palindrome(''))
print(palindrome('radar'))
print(palindrome('halibut'))

"""
このコードはデックの使い方の単純な例として使ったまでであり、高速な回文チェッカーが本当に必要なら、逆順の文字列と比較した方が
はるかに簡単だ。Pythonは、文字列で使えるrevere()を持っていないが、スライスを使えば逆順の文字列を作ることができる。
"""


def anothe_palindrome(word):
    return word == word[::-1]


print(anothe_palindrome('radar'))
print(anothe_palindrome('halibut'))
