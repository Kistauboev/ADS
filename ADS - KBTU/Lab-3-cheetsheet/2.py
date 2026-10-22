n,q=map(int,input().split())
a=list(map(int,input().split()))

for _ in range(q):
    l1,r1,l2,r2=map(int,input().split())
    print(sum(l1<=x<=r1 or l2<=x<=r2 for x in a))

""" 
from bisect import bisect_left, bisect_right

n, q = map(int, input().split())
a = sorted(map(int, input().split()))

for _ in range(q):
    l1, r1, l2, r2 = map(int, input().split())

    ans = bisect_right(a, r1) - bisect_left(a, l1)
    ans += bisect_right(a, r2) - bisect_left(a, l2)

    l = max(l1, l2)
    r = min(r1, r2)

    if l <= r:
        ans -= bisect_right(a, r) - bisect_left(a, l)

    print(ans)
    """