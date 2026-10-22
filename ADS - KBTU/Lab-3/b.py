n, q = map(int, input().split())
n1 = list(map(int, input().split()))
n1.sort()

def lower_bound(x):  # number of elements < x
    l=0
    r = len(n1)

    while l < r:
        mid = (l + r) // 2
        if n1[mid] < x:
            l = mid + 1
        else:
            r = mid
    return l

def upper_bound(x):  # number of elements <= x
    l=0
    r = len(n1)
    while l < r:
        mid = (l + r) // 2
        if n1[mid] <= x:
            l = mid + 1
        else:
            r = mid
    return l

def count(a, b):
    if a > b:
        return 0
    return upper_bound(b) - lower_bound(a)

for _ in range(q):
    l1, r1, l2, r2 = map(int, input().split())
    print(count(l1, r1) + count(l2, r2) - count(max(l1, l2), min(r1, r2)))