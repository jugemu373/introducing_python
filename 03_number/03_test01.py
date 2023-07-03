# 1時間は何秒か
seconds = 60
minutes = 60
print(seconds * minutes)

# 変数に代入
seconds_per_hour = seconds * minutes

# 1日は何秒か
print(seconds_per_hour * 24)

# 変数に代入
seconds_per_day = seconds_per_hour

# seconds_per_day を seconds_per_hourで割る
print(seconds_per_day / seconds_per_day)

# 上の除算を切り捨て除算で実行
print(seconds_per_day // seconds_per_hour)
