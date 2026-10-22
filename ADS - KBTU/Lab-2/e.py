class Node:
  def __init__(self, value):
    self.value=value       # box inside the train car, holds the runner's number
    self.next=None         # hook on the back, connects to the next car - empty at first

def deleteMiddle():
  n=int(input())                              # how many runners there are, turned into a real number
  numbers=list(map(int, input().split()))     # reads the second line, splits by space, turns each piece into int

  head=None       # sticky note for "where does the train start" - empty for now, no train yet
  tail=None       # sticky note for "where does the train currently end" - empty for now

  for num in numbers:
    new_node=Node(num)       # build a brand new car, put the current runner's number inside its box

    if head is None:         # is this the very first car we've built?
      head=new_node          # yes -> this car is both the first AND last car right now
      tail=new_node
    else:                     # not the first car, train already exists
      tail.next=new_node      # hook the old last car onto this new car
      tail=new_node            # move the tail label forward onto this new car

  if head.next is None:      # only one runner total (n=1) -> that one runner IS the middle
    head=None                 # wipe the whole train so it prints as an empty line later
  else:
    slow=head                 # slow finger starts at the very first car
    fast=head.next.next       # fast finger starts 2 cars ahead

    while fast and fast.next:   # keep going as long as fast still has room to jump 2 more steps
      slow=slow.next            # slow moves forward 1 car
      fast=fast.next.next       # fast moves forward 2 cars

    slow.next=slow.next.next    # skip trick: slow's hook jumps over the middle car, deleting it

  result=[]           # empty basket to collect the final values as text
  p=head               # walking finger, starts at the (possibly updated) head

  while p is not None:            # walk all the way to the end of the train
    result.append(str(p.value))   # put this car's number into the basket, as text
    p=p.next                       # move forward to the next car

  print(' '.join(result))   # join the basket with spaces and print it all on one line

if __name__=="__main__":
  deleteMiddle()   # actually run the whole recipe