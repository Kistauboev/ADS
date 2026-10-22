import sys
import heapq

def main():
    data = sys.stdin.read().split()
    n, m = int(data[0]), int(data[1])
    h = [-int(v) for v in data[2:2+n]]
    heapq.heapify(h)

    total = 0
    for _ in range(m):
        top = -h[0]
        total += top
        if top > 1:
            heapq.heapreplace(h, -(top - 1))
        else:
            heapq.heappop(h)
    print(total)

main()