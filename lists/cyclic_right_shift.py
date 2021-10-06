from lists.delete_from_list import print_list
from lists.node import Node

def list_len(head):
    count = 0
    while head:
        head = head.next
        count += 1

    return count


def right_shift(head, k):
    n = list_len(head)
    k = k % n

    if k == 0:
        return head

    forward, backward = head, head
    for _ in range(k):
        forward = forward.next

    while forward.next:
        forward = forward.next
        backward = backward.next

    new_head = backward.next
    backward.next = None
    forward.next = head
    return new_head


if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7
    new_head = right_shift(n1, 7)
    print_list(new_head)

