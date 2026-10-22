
class Node:
  def __init__(self, data):   # it is a boy just holding cards, nothing else
    self.data=data
    self.next=None

def main():
  n=input()
  numbers=list(map(int, input().split()))

  head=None       # we do not know, head has value or not that is way, it is none
  previous=None

  for x in numbers:
    new_node=Node(x)     # here x enters inside numbers: then we assign it to new_node, but we do not know which positition 
    if head is None:     # if head is Empty
      head=new_node
      tail=new_node
    else:
      tail.next=new_node    # this part head already have value, that is why tail=new_node
      tail=new_node

  current=head

  while current:
    temp=current.next
    current.next=previous
    previous=current
    current=temp
  new_head=previous

  result=[]
  p=new_head
  while p is not None:
    result.append(str(p.data))
    p=p.next

  print(" ".join(result))

if __name__=="__main__":
  main()

