class Node:
  def __init__(self, data):
    self.data=data
    self.next=None

def removeDuplicates():
  n=int(input())
  names=[input().strip() for i in range(n)]

  head=None    # "poyezdning ENG BOSHI qayerda" deb eslab turadi
  tail=None    # "poyezdning ENG OXIRI qayerda" deb eslab turadi

  for c in names:
    new_node=Node(c)  # Alice

    if head is None:
      head=new_node       # this part we gave first value to head
      tail=new_node
    else:
      tail.next=new_node   #  first one is taken, so we give second value  
      tail=new_node      

  current=head              # we are assigning head to current, because head is need for us to keep the first value permanently, 

  while current is not None and current.next is not None:
    if current.data==current.next.data:   # dana = dana
      current.next=current.next.next
    else:
      current=current.next

  count=0
  result=[]
  p=head

  while p is not None:
    result.append(str(p.data))
    count=count+1
    p=p.next
  print(" ".join(result))
  print('\n'.join(result))

if __name__=='__main__':
  removeDuplicates()