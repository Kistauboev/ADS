import sys

data = sys.stdin.read().split()
n = int(data[0])
dates = data[1:1 + n]

dates.sort(key=lambda d: (int(d[6:]), int(d[3:5]), int(d[:2])))

print("\n".join(dates))