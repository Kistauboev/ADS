n, t = map(int, input().split())
lst = list(map(int, input().split()))
# print(lst)
def ghoul(nums, k):
    l = max(nums)
    r = sum(nums)
    while l < r:
        m = (l + r) // 2
        temp  = 0
        cnt = 0
        for i in nums:
            if temp + i > m:
 
                cnt += 1
                temp = i
            else:
                temp += i
        if cnt + 1 > k:
            l = m + 1
        else:
            r = m
  
    return l
print(ghoul(lst, t))