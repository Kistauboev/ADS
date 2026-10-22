# Lowest Value
class Node:
  def __init__(self, data):
    self.data=data
    self.next=None

def LowestValue(head):
  minValue=head.data   # 20
  nextValue = head.next # 4

  while nextValue:
    if nextValue.data<minValue:  # 4 < 20
      minValue=nextValue.data    # min=4
    nextValue=nextValue.next     # 15

  return minValue

head=Node(20)
head.next=Node(4)
head.next.next=Node(15)
head.next.next.next=Node(1)
head.next.next.next.next=Node(8)

print(LowestValue(head))

  # 20 -> 4 -> 15 -> 1 -> 8
