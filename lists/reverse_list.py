from lists.node import Node


def reverse_list(head):
    prev = None
    cur = head
    next = head.next
    while cur is not None:
        cur.next = prev
        prev = cur
        cur = next
        if next:
            next = next.next

    return prev


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

    new_head = reverse_list(n1)

    while new_head:
        print(new_head.val)
        new_head = new_head.next
