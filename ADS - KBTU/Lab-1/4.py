n=int(input())

def is_prime(x):
  if x<=1:
    return False
  else:
    for a in range(2,x):
      if(x%a==0):
        return False
  return True

count=0       # how many primes we've found so far
number=1      # the number we're currently testing to see if it's prime

while count<n:
  number=number+1
  if(is_prime(number)):
    count=count+1
print(number)