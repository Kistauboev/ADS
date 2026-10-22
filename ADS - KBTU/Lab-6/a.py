n=int(input())
s=input().strip()

print("".join(sorted(s, key=lambda ch: (ch not in "aeiou", ch))))