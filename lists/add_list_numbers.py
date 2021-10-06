from lists.delete_from_list import print_list
from lists.node import Node


def add_lists(head1, head2):
    new_tail = Node(0)
    head = new_tail
    carry = 0

    while head1 and head2:
        new_tail.val = (head1.val + head2.val + carry) % 10
        carry = (head1.val + head2.val) // 10
        new_tail.next = Node(0)
        new_tail = new_tail.next
        head1 = head1.next
        head2 = head2.next

    while head1:
        new_tail.val = (head1.val + carry) % 10
        carry = (head1.val + carry) // 10
        if head1.next:
            new_tail.next = Node(0)
            new_tail = new_tail.next
        head1 = head1.next

    while head2:
        new_tail.val = (head2.val + carry) % 10
        carry = (head2.val + carry) // 10
        if head2.next:
            new_tail.next = Node(0)
            new_tail = new_tail.next
        head2 = head2.next

    return head


if __name__ == "__main__":
    l11 = Node(1)
    l13 = Node(3)
    l15 = Node(5)
    l17 = Node(7)

    l22 = Node(2)
    l24 = Node(4)
    l26 = Node(6)

    l11.next = l13
    l13.next = l15
    l15.next = l17

    l22.next = l24
    l24.next = l26
    list = add_lists(l11, l22)
    print_list(list)
