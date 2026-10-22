n = int(input())
ages = list(map(int, input().split()))

stack = []
answers = []

for age in ages:
    while len(stack) > 0 and stack[-1] >= age:
        stack.pop()
    if len(stack) == 0:
        answers.append(-1)
    else:
        answers.append(stack[-1])
    stack.append(age)

print(*answers)