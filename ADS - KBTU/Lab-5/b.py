import sys
import heapq

def main():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
    n = int(data[0])
    h = [-int(v) for v in data[1:1+n]]
    heapq.heapify(h)

    while len(h) > 1:
        y = -heapq.heappop(h)  
        x = -h[0]              
        if y == x:
            heapq.heappop(h)   
        else:
            heapq.heapreplace(h, -(y - x))  

    print(-h[0] if h else 0)

main()