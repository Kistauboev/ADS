import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

def solve():
    head = None
    tail = None
    output = []
    
    for line in sys.stdin:
        line = line.rstrip('\n')
        if not line:
            continue
        parts = line.split(' ', 1)
        cmd = parts[0]
        
        if cmd == 'add_front':
            title = parts[1]
            node = Node(title)
            if head is None:
                head = tail = node
            else:
                node.next = head
                head.prev = node
                head = node
            output.append('ok')
        
        elif cmd == 'add_back':
            title = parts[1]
            node = Node(title)
            if tail is None:
                head = tail = node
            else:
                node.prev = tail
                tail.next = node
                tail = node
            output.append('ok')
        
        elif cmd == 'erase_front':
            if head is None:
                output.append('error')
            else:
                output.append(head.value)
                head = head.next
                if head is not None:
                    head.prev = None
                else:
                    tail = None
        
        elif cmd == 'erase_back':
            if tail is None:
                output.append('error')
            else:
                output.append(tail.value)
                tail = tail.prev
                if tail is not None:
                    tail.next = None
                else:
                    head = None
        
        elif cmd == 'front':
            output.append(head.value if head is not None else 'error')
        
        elif cmd == 'back':
            output.append(tail.value if tail is not None else 'error')
        
        elif cmd == 'clear':
            head = None
            tail = None
            output.append('ok')
        
        elif cmd == 'exit':
            output.append('goodbye')
            break
    
    print('\n'.join(output))

solve()
