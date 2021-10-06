from lists.delete_from_list import print_list
from lists.node import Node


def odd_even_merge(head):
    cur = head
    next = head.next
    is_odd = True
    even_head = next
    odd_tail = next

    while next:
        cur.next = next.next
        if is_odd:
            odd_tail = cur
        cur = next
        next = next.next
        is_odd = not is_odd

    odd_tail.next = even_head
    return head


if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n8 = Node(8)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7
    n7.next = n8
    new_head = odd_even_merge(n1)
    print_list(new_head)
