from datetime import datetime, timedelta

# 获取当前日期和时间
now = datetime.now()
print(now.year, now.month, now.day, now.hour, now.minute, now.second, now.timestamp(), )
print("时间戳时间秒数：", int(now.timestamp()))
print("时间戳时间毫秒数：", int(now.timestamp() * 1000))

# 修改日期
now = now + timedelta(days=10)
now = now + timedelta(hours=1)
now = now + timedelta(minutes=10)
now = now + timedelta(seconds=10)
print(now)

# 日期求差
date1 = datetime(2023, 1, 1)
date2 = datetime(2024, 2, 1)
difference = date2 - date1
print(difference.days)  # 相差天数
print(difference.total_seconds())  # 相差秒数
