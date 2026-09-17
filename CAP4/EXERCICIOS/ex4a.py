class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


head = None
for data in range(1, 6):
    head = Node(data, head)

probe = head
while probe is not None:
    print(f"[{probe.data}] -> ", end="")
    probe = probe.next
print("None")
