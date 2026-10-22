a, n, m = map(int, input().split())

result = 1%m     # this matters when m=1, since then 1 % 1 = 0, which is correct (everything mod 1 is 0)
a = a % m       # (a = 3 % 7 = 3) - just an example

while n > 0:
    if n % 2 == 1:
        result = (result * a) % m
    a = (a * a) % m
    n = n // 2

print(result)