class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def cutList():
    n, m = map(int, input().split())
    words = input().split()

    head = None
    tail = None

    for word in words:
        new_node = Node(word)

        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node

    current = head

    for i in range(m - 1):
        current = current.next

    temp = current.next
    tail.next = head
    current.next = None
    head = temp

    current = head

    while current is not None:
        print(current.value, end=" ")
        current = current.next


cutList()