import sys

def sift_down(h, i, n):
    x = h[i]
    while True:
        l = 2*i + 1
        if l >= n:
            break
        r = l + 1
        if r < n and h[r] < h[l]:
            l = r
        if h[l] < x:
            h[i] = h[l]
            i = l
        else:
            break
    h[i] = x

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    h = list(map(int, data[1:1+n]))

    for i in range(n//2 - 1, -1, -1):
        sift_down(h, i, n)

    total = 0
    while n > 1:
      
        x = h[0]
        last = h.pop()
        n -= 1
        h[0] = last
        sift_down(h, 0, n)
     
        s = x + h[0]
        total += s
        h[0] = s
        sift_down(h, 0, n)
    print(total)

main()