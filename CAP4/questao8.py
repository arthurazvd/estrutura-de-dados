class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def length(head):
    total = 0
    probe = head
    while probe is not None:
        total += 1
        probe = probe.next
    return total


head = Node(10, Node(20, Node(30)))
print("Tamanho:", length(head))
