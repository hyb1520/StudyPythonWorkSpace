from datetime import datetime

now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))

dt = datetime(2016, 5, 11, 13, 15, 15)
print(dt.timestamp())

t = 1462943715.0
print(datetime.utcfromtimestamp(t))
