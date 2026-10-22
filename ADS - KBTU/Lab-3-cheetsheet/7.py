n,k=map(int,input().split())
a=list(map(int,input().split()))

l,r=0,max(a)

for _ in range(100):
    m=(l+r)/2

    if sum(int(x/m) for x in a)>=k:
        l=m
    else:
        r=m

print(f"{l:.9f}")