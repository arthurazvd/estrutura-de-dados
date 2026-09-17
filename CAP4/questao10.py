class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def length(head):
    total = 0
    while head is not None:
        total += 1
        head = head.next
    return total


def pop(position, head):
    if position < 0 or position >= length(head):
        raise IndexError("Posição fora da estrutura")
    if position == 0:
        return head.next, head.data

    probe = head
    for count in range(position - 1):
        probe = probe.next
    removed = probe.next
    probe.next = removed.next
    return head, removed.data


head = Node(10, Node(20, Node(30)))
head, item = pop(1, head)
print("Removido:", item)
while head is not None:
    print(head.data, end=" ")
    head = head.next
print()
