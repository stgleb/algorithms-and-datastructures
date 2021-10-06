from lists.delete_from_list import print_list
from lists.node import Node


def remove_duplicates(head):
    if head is None:
        return
    start, end = head, head

    while start:
        while end and start.val == end.val:
            end = end.next
        start.next = end
        start = end


if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(2)
    n4 = Node(4)
    n5 = Node(6)
    n6 = Node(6)
    n7 = Node(7)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7
    remove_duplicates(n1)
    print_list(n1)
