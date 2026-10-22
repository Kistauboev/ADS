# class Node:
#      def __init__(self, value):
#          self.value = value
#          self.next = None

# def solve():
#      n = int(input())
#      values = list(map(int, input().split()))

#      head = Node(values[0])
#      current = head
#      for v in values[1:]:
#          current.next = Node(v)
#          current = current.next
    
#      # now delete every second node
#      current = head
#      while current is not None and current.next is not None:
#          current.next = current.next.next
#          # move to the next "kept" node
#          current = current.next
    
#      result = []
#      node = head
#      while node is not None:
#          result.append(str(node.value))
#          node = node.next
    
#      print(' '.join(result))

# solve()


class Node:
  def __init__(self, data):   # it is a boy just holding cards, nothing else
    self.data=data
    self.next=None

def main():
  n=input()
  numbers=list(map(int, input().split()))

  head=None       # we do not know, head has value or not that is way, it is none
  tail=None

  for x in numbers:
    new_node=Node(x)     # here x enters inside numbers: then we assign it to new_node, but we do not know which positition 
    if head is None:     # if head is Empty
      head=new_node
      tail=new_node
    else:
      tail.next=new_node    # this part head already have value, that is why tail=new_node
      tail=new_node

  current=head

  while current is not None and current.next is not None:
    to_delete=current.next       #   this part is pointing to next value    2 
    current.next=to_delete.next   
    current=current.next    

  result=[]
  p=head
  while p is not None:
    result.append(str(p.data))
    p=p.next
  print(" ".join(result))

if __name__=='__main__':
  main()




  # head = "the permanent bookmark that NEVER moves, marking the start"
  # current = "a temporary, movable finger I use to walk down the train and do work"