class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class TwoWayNode(Node):
    def __init__(self, data, previous=None, next=None):
        super().__init__(data, next)
        self.previous = previous


def makeTwoWay(head):
    new_head = None
    tail = None
    probe = head

    while probe is not None:
        new_node = TwoWayNode(probe.data, tail)
        if new_head is None:
            new_head = new_node
        else:
            tail.next = new_node
        tail = new_node
        probe = probe.next
    return new_head


original = Node(10, Node(20, Node(30)))
two_way = makeTwoWay(original)

tail = two_way
while tail.next is not None:
    tail = tail.next
while tail is not None:
    print(tail.data, end=" ")
    tail = tail.previous
print()
