def process(s):
    stack = []
    for ch in s:
        if ch == '#':
            if len(stack) > 0:   #check just guards against a weird edge case: what if # appears at the very start, with nothing typed yet? Then there's nothing to delete, so we just skip it instead of crashing.
                stack.pop()
        else:
            stack.append(ch)
    return ''.join(stack)

s1 = input()
s2 = input()

if process(s1) == process(s2):
    print("Yes")
else:
    print("No")