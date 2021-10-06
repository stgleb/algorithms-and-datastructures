import lists.delete_from_list
from lists.node import Node


def remove_kth_element(head, k ):
    forward, backward = head, head
    for _ in range(k):
        if forward:
            forward = forward.next

    if forward is None:
        return

    while forward.next:
        forward = forward.next
        backward = backward.next

    if backward.next:
        backward.next = backward.next.next


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

    remove_kth_element(n1, 3)
    lists.delete_from_list.print_list(n1)
