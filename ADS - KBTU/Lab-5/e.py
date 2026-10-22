import sys
import heapq

def main():
    data = sys.stdin.read().split()
    q, k = int(data[0]), int(data[1])
    h = []
    total = 0
    out = []
    p = 2
    for _ in range(q):
        cmd = data[p]
        p += 1
        if cmd == "insert":
            x = int(data[p])
            p += 1
            if len(h) < k:
                heapq.heappush(h, x)
                total += x
            elif x > h[0]:
                total += x - h[0]
                heapq.heapreplace(h, x)
        else:
            out.append(total)
    if out:
        print("\n".join(map(str, out)))

main()