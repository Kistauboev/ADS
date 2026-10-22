import sys

data = sys.stdin.read().split()
n = int(data[0])

cur = {}  # current nickname -> original nickname
for i in range(n):
    old, new = data[1 + 2 * i], data[2 + 2 * i]
    orig = cur.pop(old, old)
    cur[new] = orig

pairs = sorted((orig, now) for now, orig in cur.items())

out = [str(len(pairs))]
for orig, now in pairs:
    out.append(orig + " " + now)
print("\n".join(out))