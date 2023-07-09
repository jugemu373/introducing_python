# =による代入
# 辞書に変更を加えると、その辞書を参照している全ての名前に影響が及ぶ
signals = {
    'green': 'go',
    'yellow': 'go faster',
    'red': 'smile for the camera'
}
save_signals = signals
signals['blue'] = 'confuse everyone'
print(save_signals)
