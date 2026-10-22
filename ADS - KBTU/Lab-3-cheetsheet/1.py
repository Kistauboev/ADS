n=int(input())
a=list(map(int,input().split()))
x=int(input())

print("Yes" if x in a else "No")


""" 
n = int(input())
a = list(map(int, input().split()))
x = int(input())

l, r = 0, n - 1

while l <= r:
    m = (l + r) // 2

    if a[m] == x:
        print("Yes")
        break
    elif a[m] < x:
        l = m + 1
    else:
        r = m - 1
else:
    print("No") 
    """