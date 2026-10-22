from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    slots = deque(range(1, n + 1))
    result = [0] * (n + 1)
    k = 1
    while slots:
        m = len(slots)
        eff = k % m
        if eff:
            slots.rotate(-eff)
        top = slots.popleft()
        result[top] = k
        k += 1
    print(*result[1:])