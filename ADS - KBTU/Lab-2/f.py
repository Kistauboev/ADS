class Node:
  def __init__(self, value):
    self.value=value
    self.next=None

def mergeList():
  head1=None
  tail1=None

  head2=None
  tail2=None

  values1=list(map(int, input().split()))
  n1=values1[0]
  number1=values1[1: ]

  values2=list(map(int, input().split()))
  n2=values2[0]
  number2=values2[1:]

  for num1 in number1:
    new_node=Node(num1)
    if head1 is None:
      head1=new_node
      tail1=new_node
    else:
      tail1.next=new_node
      tail1=new_node

  for num2 in number2:
    new_node=Node(num2)
    if head2 is None:
      head2=new_node
      tail2=new_node
    else:
      tail2.next=new_node
      tail2=new_node

  dummy=Node(0)         # dummy is a fake first car that keeps your place at the start of the merged list.
  merged_tail=dummy

  while head1 and head2:   # since both lists still have cars
    if head1.value<head2.value:
      merged_tail.next=head1
      head1=head1.next
    else:
      merged_tail.next=head2
      head2=head2.next
    merged_tail=merged_tail.next

  if head1:
    merged_tail.next=head1
  else:
    merged_tail.next=head2

  results=[]
  p=dummy.next
  while p is not None:
    results.append(str(p.value))
    p=p.next

  print(' '.join(results))

if __name__=="__main__":
  mergeList()

