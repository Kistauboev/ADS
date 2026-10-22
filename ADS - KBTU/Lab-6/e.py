import sys

data = sys.stdin.read().split()
n, m = int(data[0]), int(data[1])
vals = list(map(int, data[2:2 + n * m]))

cols = []
for j in range(m):
    col = [vals[i * m + j] for i in range(n)]
    col.sort(reverse=True)
    cols.append(col)

out = []
for i in range(n):
    out.append(" ".join(str(cols[j][i]) for j in range(m)))

print("\n".join(out))