from bisect import *

n,m=map(int,input().split())
a=list(map(int,input().split()))

for i in range(1,n):
    a[i]+=a[i-1]

for _ in range(m):
    print(bisect_left(a,int(input()))+1)
""" 
from bisect import bisect_left

n, m = map(int, input().split())
a = list(map(int, input().split()))

pref = []
s = 0

for x in a:
    s += x
    pref.append(s)

for _ in range(m):
    x = int(input())
    print(bisect_left(pref, x) + 1)
    """