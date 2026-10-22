import sys

data = sys.stdin.read().split()
n = int(data[0])
arr = data[1:1 + n]
x = data[1 + n]
ans = arr[0]          # wrap-around default
for ch in arr:
    if ch > x:
        ans = ch
        break

print(ans)



# import heapq

# heapq.heapify(h)
# ans = h[0]
# while h:
#     t = heapq.heappop(h)
#     if t > x:
#         ans = t
#         break
# print(ans)