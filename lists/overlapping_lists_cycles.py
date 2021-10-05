from lists.node import Node


def has_cycles(head):
    fast, slow = head, head

    fast = fast.next
    if fast:
        fast = fast.next
    slow = slow.next
    while fast and slow and fast is not slow:
        fast = fast.next
        if fast:
            fast = fast.next
        slow = slow.next

    if fast is not slow:
        return None

    slow = head
    while fast != slow:
        slow = slow.next
        fast = fast.next

    return slow


def find_overlapping_cycles(head1, head2):
    base1 = has_cycles(head1)
    base2 = has_cycles(head2)

    if base1 is None or base2 is None:
        return None

    first = base1
    while base1.next != first and base1 is not base2:
        base1 = base1.next

    if base1 is base2:
        return base1.val

    return None


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
    l26.next = l15
    l17.next = l13

    print(find_overlapping_cycles(l11, l22))
