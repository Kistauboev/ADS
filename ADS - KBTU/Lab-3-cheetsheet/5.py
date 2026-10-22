from bisect import *

n,q=map(int,input().split())
a=sorted(map(int,input().split()))

for _ in range(q):
    l1,r1,l2,r2=map(int,input().split())
    f=lambda l,r: bisect_right(a,r)-bisect_left(a,l)
    print(f(l1,r1)+f(l2,r2)-f(max(l1,l2),min(r1,r2)) if max(l1,l2)<=min(r1,r2) else f(l1,r1)+f(l2,r2))