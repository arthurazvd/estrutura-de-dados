class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


array = [10, 20, 30, 40]
head = None
tail = None

for item in array:
    novo = Node(item)
    if head is None:
        head = novo
    else:
        tail.next = novo
    tail = novo

probe = head
while probe is not None:
    print(probe.data)
    probe = probe.next
