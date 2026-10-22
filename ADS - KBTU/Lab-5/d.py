import sys
import heapq

def main():
    data = sys.stdin.read().split()
    n, k = int(data[0]), int(data[1])
    h = list(map(int, data[2:2+n]))
    heapq.heapify(h)

    ops = 0
    while h[0] < k:
        if len(h) < 2:
            print(-1)
            return
        x = heapq.heappop(h)
        y = heapq.heappop(h)
        heapq.heappush(h, x + 2 * y)
        ops += 1
    print(ops)

main()