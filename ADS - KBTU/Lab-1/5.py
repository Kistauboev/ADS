n=int(input())

d=2
factors=[]

while d*d<=n:
  while n%d==0:
    factors.append(d)
    n=n//d
  d=d+1

if n>1:
  factors.append(n)

print(*factors)
  
# PRIME FACTORIZATION - check it is divisible by 2 or not. 