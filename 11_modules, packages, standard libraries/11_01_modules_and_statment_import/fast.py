"""モジュール"""
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

def pick(): # 下にdockstringがあることに注目
    """ランダムなファーストフード店の名前を返す"""
    return choice(places)
