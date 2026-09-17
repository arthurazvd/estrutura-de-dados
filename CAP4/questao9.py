class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def insert(item, position, head):
    if position <= 0 or head is None:
        return Node(item, head)

    probe = head
    while position > 1 and probe.next is not None:
        probe = probe.next
        position -= 1
    probe.next = Node(item, probe.next)
    return head


def display(head):
    probe = head
    while probe is not None:
        print(probe.data, end=" ")
        probe = probe.next
    print()


head = None
head = insert(10, 0, head)
head = insert(30, 1, head)
head = insert(20, 1, head)
head = insert(40, 99, head)
display(head)
