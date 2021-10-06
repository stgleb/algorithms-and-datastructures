from lists.delete_from_list import print_list
from lists.node import Node


def pivot(head, pivot_val):
    pt = head
    cur = head
    while cur:
        if cur.val <= pivot_val:
            pt.val, cur.val = cur.val, pt.val
            pt = pt.next
        cur = cur.next


if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(3)
    n3 = Node(5)
    n4 = Node(4)
    n5 = Node(8)
    n6 = Node(2)
    n7 = Node(6)
    n8 = Node(8)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7
    n7.next = n8
    pivot(n1, 5)
    print_list(n1)
