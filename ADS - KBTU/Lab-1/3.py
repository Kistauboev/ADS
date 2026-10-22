x=int(input())

if x<=1:
  print("No")
else:
  for a in range(2, x):
    if(x%a==0):
      print("No")
      break
  else:
    print("Yes")