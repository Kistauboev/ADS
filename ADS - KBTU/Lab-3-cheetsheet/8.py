n,k=map(int,input().split())
a=list(map(int,input().split()))
if k==0:
  print(1);exit()
l=s=0;z=n
for r,x in enumerate(a):
 s+=x
 while s>=k:z=min(z,r-l+1);s-=a[l];l+=1
print(z)