n,k=map(int,input().split())
a=[]
for _ in range(n):
 x,y,X,Y=map(int,input().split());a.append(max(X,Y))
print(sorted(a)[k-1])