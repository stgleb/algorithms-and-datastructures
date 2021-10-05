from lists.node import Node


def test_for_cycles(head):
    if head is None:
        return False

    fast, slow = head, head
    fast = fast.next
    if fast:
        fast = fast.next
    slow = slow.next

    while fast and slow and fast != slow:
        fast = fast.next
        if fast:
            fast = fast.next
        slow = slow.next

    if fast is None or slow is None:
        return False

    return True


def first_node_in_cycle(head):
    fast, slow = head, head
    fast = fast.next
    if fast:
        fast = fast.next
    slow = slow.next

    while fast and slow and fast != slow:
        fast = fast.next
        if fast:
            fast = fast.next
        slow = slow.next

    if fast == slow and fast is not None:
        fast = head

        while fast != slow:
            fast = fast.next
            slow = slow.next

        return fast.val

    return None


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
    n7.next = n4

    print(test_for_cycles(n1))
    print(first_node_in_cycle(n1))
