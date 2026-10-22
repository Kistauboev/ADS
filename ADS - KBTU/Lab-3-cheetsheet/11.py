q=int(input());v=list(map(int,input().split()))
n,m=map(int,input().split());d={}
for i in range(n):
 for j,x in enumerate(map(int,input().split())):d[x]=(i,j)
for x in v:
 print(*d[x]) if x in d else print(-1)