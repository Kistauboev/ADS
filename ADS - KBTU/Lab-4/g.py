
import sys

d=sys.stdin.read().split()
p=list(dict.fromkeys(map(int,d[1:1+int(d[0])])))
n=len(p)
rk={v:i+1 for i,v in enumerate(sorted(p))}
r=[rk[v] for v in p]
t=[-1]*(n+2)
for i,x in enumerate(r):
    t[x]=i
pv=list(range (-1, n+1))
nx=list(range(1, n+3))
par=[0]*(n+2)
left=[False]*(n+2)

for x in reversed(r):
    a,b=pv[x], nx[x]
    if t[a]>t[b]:
        par[x]=a
    elif t[b]>=0:
        par[x]=b
        left[x]=True
    nx[a]=b
    pv[b]=a
hl=[0]*(n+2)
hr=[0]*(n+2)
ans=0

for x in reversed(r):
    ans=max(ans,hl[x]+hr[x]+1)
    h=max(hl[x],hr[x])+1
    q=par[x]

    if q:
        if left[x]:
            hl[q]=h
        else:
            hr[q]=h
print(ans)
