import sys
d = sys.stdin.read().split()
n, k = int(d[0]), int(d[1])
a = sorted(map(int, d[2:2 + n]))
print(a[k - 1] if 1 <= k <= n else -1)