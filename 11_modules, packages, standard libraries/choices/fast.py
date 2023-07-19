"""
第2のモジュール(choices/advice.py)は新しいものだが、ファストフード選択と同じような動作をする。
"""
from random import choice


places = [
    "McDonalds",
    "KFC",
    "Burger King",
    "Taco Bell",
    "Wendys",
    "Arbys",
    "Pizza Hut"
]

def pick():
    """ランダムなファストフード店を返す"""
    return choice(places)

