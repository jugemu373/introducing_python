# shallow copyの例
import copy
signals = {
    'green': 'go',
    'yellow': 'go faster',
    'red': ['stop', 'smile'],
}
signals_copy = signals.copy()
print(signals)
print(signals_copy)

# redリストの片方の値を書き換える
signals['red'][1] = 'sweat'
print(signals)
print(signals_copy)

# deepcopy()は完全なコピーを生成
signals = {
    'green': 'go',
    'yellow': 'go faster',
    'red': ['stop', 'smile'],
}
signals_copy = copy.deepcopy(signals)
print(signals)
print(signals_copy)
signals['red'][1] = 'sweat'
print(signals)
print(signals_copy)
