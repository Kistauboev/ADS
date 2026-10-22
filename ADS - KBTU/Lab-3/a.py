"""
a=int(input())
b=list(map(int, input().split()))
target=int(input())


def binary_search():

  l=0           # starts from left at index 0
  r=len(b)-1    # starts from last index. for instance we have 5 numbers, so last index is 4 = last number
  mid=0

  while l<=r:
    mid=(l+r)//2       # mid pozitsiyani topadi
    
    if b[mid]==target:
      return mid
    elif b[mid]<target:
      l=mid+1
    else:
      r=mid-1
  return -1

if binary_search()!= -1:
  print("Yes")
else:
  print("No")



"""

a=int(input())
b=list(map(int, input().split()))
target=int(input())

def binary_search():
  l=0
  r=len(b)-1
  mid=0

  while l<=r:
    mid=(l+r)//2
    if b[mid]<target:
      l=mid+1
    elif b[mid]>target:
      r=mid-1
    else:
      return mid
  return -1

if binary_search()!=-1:
  print("Yes")
else:
  print("No")