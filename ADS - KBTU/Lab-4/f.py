import sys

d=sys.stdin.read().split()
n=int(d[0])
p=list(map(int, d[1:1+n]))
s=sorted(p)
rk={v:i+1 for i, v in enumerate(s)}
r=[rk[v] for v in p]
t=[0]*(n+2)

for i,x in enumerate(r):
    t[x]=i
t[0]=t[n+1]=-1
prv=list(range(-1, n+1))
nxt=list(range(1, n+3))

L=[False]*(n+2)
R=[False]*(n+2)
for x in reversed(r):
    a,b=prv[x],nxt[x]
    if t[a]>t[b]:
        R[a]=True
    elif t[b]>=0:
        L[b]=True
    nxt[a]=b
    prv[b]=a

print(sum(1 for i in range(1, n+1) if L[i] and R[i]))