n=int(input())
p=list(map(int, input().split()))
prv=list(range(-1,n+1))
nxt=list(range(1, n+3))
A=[0]*(n+2);
B=[0]*(n+2)

for x in reversed(p):
    a,b=prv[x],nxt[x]
    A[x],B[x]=a,b
    nxt[a]=b;
    prv[b]=a
d=[0]*(n+2)
s=[0]*(n+2)

for x in p:
    d[x]=max(d[A[x]], d[B[x]])+1
    s[d[x]]+=x
m=max(d)
print(m)
print(*s[1:m+1])