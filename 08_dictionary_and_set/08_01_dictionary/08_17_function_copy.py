# copy()は、別の辞書に実際にキー/バリューをコピーできる
# copy()は、shallow copyである
signals = {
    'green': 'go',
    'yellow': 'go faster',
    'red': 'smile for the camera',
}
original_signals = signals.copy()
signals['blue'] = 'confuse everyone'
print(signals)
print(original_signals)
