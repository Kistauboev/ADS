class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def maxSubarray():
    n = int(input())
    values = list(map(int, input().split()))

    head = None
    tail = None

    for value in values:
        new_node = Node(value)

        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node

    current = head  # Okay, let's start looking at the first number.

    best = current.value
    current_sum = current.value   # How much money is in my current bag?

    current = current.next      # Move to the next number

    while current is not None:
        current_sum = max(current.value, current_sum + current.value)
        best = max(best, current_sum)

        current = current.next

    print(best)


maxSubarray()