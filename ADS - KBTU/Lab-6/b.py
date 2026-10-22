import sys
from collections import Counter

data = sys.stdin.read().split()
n, m = int(data[0]), int(data[1])
a = list(map(int, data[2:2 + n]))
b = list(map(int, data[2 + n:2 + n + m]))

ca, cb = Counter(a), Counter(b)
res = []
for x in sorted(ca):
    if x in cb:
        res.extend([x] * min(ca[x], cb[x]))

print(" ".join(map(str, res)))