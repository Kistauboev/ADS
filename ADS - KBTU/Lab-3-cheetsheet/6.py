n,h=map(int,input().split())
a=list(map(int,input().split()))
l,r=1,max(a)

while l<r:
    m=(l+r)//2
    if sum((x+m-1)//m for x in a)<=h:r=m
    else:l=m+1

print(l)