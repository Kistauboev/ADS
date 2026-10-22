s = input()
stack = []

for ch in s:
    if len(stack) > 0 and stack[-1] == ch:
        stack.pop()
    else:
        stack.append(ch)

if len(stack) == 0:
    print("YES")
else:
    print("NO")